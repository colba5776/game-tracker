import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect
from login_register import login, register
from manage_games import manage_games

# Establish a connection, create a cursor and set it to use gametrackerdb
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

def main():
    # Ask if they wish to login or register until they enter either L or R
    userInput = None
    while (userInput != 'R' and userInput != 'L'):
        userInput = input("Enter [L] to Login, [R] to Register: ")
    # Check if they chose to register and run the register function if we did
    if (userInput == 'R'):
        register()
    # Keep requesting login information until valid credentials are provided (userId is no longer None)
    userId = None
    while userId is None:
        userId = login()

    # Maybe list out some cool stats? Like recently completed playthroughs, list of games, etc..

    # While the user is not done
    done = False
    while (not done):
        # Ask the user where they would like to go
        userInput = None
        while (userInput != 'Games' and userInput != 'Playthroughs' and userInput != 'Ratings' and userInput != 'Quit'):
            userInput = input("Where would you like to go?\nEnter [Games], [Playthroughs], [Ratings], or [Quit] to Quit: ")
        # If they wish to go to games
        if (userInput == 'Games'):
            manage_games(userId)
        if (userInput == 'Quit'):
            done = True
    
    close_connection()

""" Ends the connection to the MySQL server """
def close_connection():
    conn.close()
    print('Connection closed.')

if __name__ == "__main__":
    main()