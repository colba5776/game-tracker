import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

# Establish a connection, create a cursor and set it to use gametrackerdb
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

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
            userInput = input("Do these credentials look good?\nEnter [Y] to confirm, [N] to update credentials: ")    
            if (userInput == 'Y'):
                confirmed = True
                # Insert the new user into the database
                cursor.execute(f"INSERT INTO user (userName, userPassword) VALUES ('{userName}', '{userPassword}');")
                conn.commit()
                # Ask the user to enter their login credentials
                print("Please log in with your new credentials.")

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
