import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

# Establish a connection, create a cursor and set it to use gametrackerdb
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

def main():
    # Keep requesting login information until valid credentials are provided (userId is no longer None)
    userId = None
    while userId is None:
        userId = login()
    
    # Display list of all games
    cursor.execute("SELECT * FROM game;")
    pt = from_db_cursor(cursor)
    pt.field_names = ["Game ID", "Title", "Description", "Genre", "Owner"]
    pt.del_column("Game ID")
    pt.align["Title"] = "l"
    pt.del_column("Description")
    pt.align["Genre"] = "l"
    pt.align["Owner"] = "l"
    pt.sortby = "Title"
    print(pt)

    close_connection()

""" Ends the connection to the MySQL server """
def close_connection():
    conn.close()
    print('Connection closed.')

""" Used to run user login procedure """ 
def login():
    # Where we will store the userId if we find it
    userId = None
    # Ask user for their userName
    userName = input("Enter your username: ")
    # Ask user for their userPassword
    userPassword = input("Enter your password: ")
    
    # Search for a userId with matching userName and userPassword
    cursor.execute(f"SELECT userId FROM user WHERE userName='{userName}' AND userPassword='{userPassword}';")
    result = cursor.fetchone() # Get the resulting row for the query
    
    # Check if we successfully found a user with the matching credentials and return the userId if we did
    if result is not None:
        userId = int(result[0])
        print(f"Welcome {userName}!")
    else:
        print("Invalid credentials.")
    # Return the value of userId
    return userId

if __name__ == "__main__":
    main()

"""
prettytable = from_db_cursor(cursor)
prettytable.align["userName"] = "l"
prettytable.sortby = "userName"
print(prettytable)
"""