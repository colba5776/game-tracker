import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

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
    if (result is not None):
        userId = int(result[0])
        print(f"Welcome {userName}!")
    else:
        print("Invalid credentials.")
    # Return the value of userId
    return userId

""" Used to run user register procedure """ 
def register():
    # Where we will store whether the player has confirmed their information or not
    confirmed = False
    while (confirmed == False):
        # Ask user for their userName
        userName = input("Enter your desired username: ")
        # Ask user for their userPassword
        userPassword = input("Enter your desired password: ")
        
        # Search for a userId with matching userName to see if it's available
        cursor.execute(f"SELECT userId FROM user WHERE userName='{userName}';")
        result = cursor.fetchone() # Get the resulting row for the query
        
        # Check if we successfully found a user with the matching userName
        if (result is not None):
            print(f"Username ({userName}) is not available.")
        else:  
            userInput = input("Do these credentials look good?\n Enter [Y] to confirm, [N] to update credentials: ")    
            if (userInput == 'Y'):
                confirmed = True
                # Insert the new user into the database
                cursor.execute(f"INSERT INTO user (userName, userPassword) VALUES ('{userName}', '{userPassword}');")
                conn.commit()
    

if __name__ == "__main__":
    main()

"""
prettytable = from_db_cursor(cursor)
prettytable.align["userName"] = "l"
prettytable.sortby = "userName"
print(prettytable)
"""