import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

# Establish a connection, create a cursor and set it to use gametrackerdb
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

def manage_ratings(userId):
    # List out all the ratings in the database
    list_ratings(None, None)
    # While the user still wants to do something here
    done = False
    while (not done):
        # Ask whether the user would like to view games, or edit them
        userInput = None
        while (userInput != 'S' and userInput != 'C' and userInput != 'B'):
            userInput = input("Enter [S] to Search, [C] to Create, [B] to go Back: ")
        # If they wish to search for a game
        if (userInput == 'S'):
            # Display list of all games
            search_ratings()
        # If they wish to create a review
        if (userInput == 'C'):
            create_rating(userId)
        # If they wish to leave
        if (userInput == 'B'):
            done = True

def search_ratings():
    # Ask the user what they would like to search by
    userInput = None
    while (userInput != 'U' and userInput != 'G'):
        userInput = input("What would you like to search by? Enter [U] for Username, [G] for Game: ")
    # Check if they want to search by userName
    if (userInput == 'U'):
        userName = None
        while (userName == None):
            # Get the userName they wish to search by
            userName = input("Enter the username you want to search by: ")
            # Get the userId for the userName and double check that it exists
            cursor.execute(f"SELECT userId FROM user WHERE userName='{userName}';")
            result = cursor.fetchone() # Get the resulting row for the query
            if (result is None):
                print(f"User {userName} does not exist!")
                userName = None
        # Get the userId
        userId = result[0]
        # List out all ratings created by the corresponding userId
        print(f"----- List of ratings by {userName} -----")
        list_ratings(userId, None)
    # Check if they want to search by gameTitle
    if (userInput == 'G'):
        gameTitle = None
        while (gameTitle == None):
            # Get their input for the title
            gameTitle = input("Enter the title of the game you want to search for: ")
            # Get the game they are searching for
            cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
            result = cursor.fetchone() # Get the resulting row for the query
            if (result is None):
                print(f"{gameTitle} does not exist!")
                gameTitle = None
        # Get the gameId
        gameId = result[0]
        # Display ratings for game with gameId
        list_ratings(None, gameId)

""" Used to add a new rating to the database """ 
def create_rating(userId): 
    # Ask user for the name of the game they wish to review
    gameTitle = None
    while (gameTitle == None):
        gameTitle = input("Please enter the title of the game you want to review: ")
        # Check if the name exists
        cursor.execute(f"SELECT gameTitle FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"{gameTitle} does not exist!")
            gameTitle = None
    # Get and store the gameId of the game they wish to review
    cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
    result = cursor.fetchone()
    gameId = result[0]
    # Get new rating information
    print("Please enter the following information for your rating:")
    # Ask the user for a number they wish to rate the game (0 -10)
    ratingValue = None
    while (ratingValue == None):
        ratingValue = input("Rating value (0 - 10): ")
        ratingValue = int(ratingValue)
        if (ratingValue < 0 or ratingValue > 10):
            print(f"{ratingValue} is not within the range 0 - 10!")
            ratingValue = None
    # Get the rating description
    ratingDescription = input("Description: ")
    # Insert the rating into the database
    cursor.execute(f"INSERT INTO rating VALUES ('{ratingValue}','{ratingDescription}','{userId}','{gameId}');")
    conn.commit()
    # Display message to tell the user it was successfull and list ratings again
    print("New rating successfully created!")
    list_ratings(None, None)

""" Used to list out all the ratings in the database """
""" If userId is not None, then only list ratings added by userId """
def list_ratings(userId, gameId):
    # Check if we only want to list ratings added by userId
    if (userId is not None):
        cursor.execute(f"SELECT ratingValue, ratingDescription, get_user_name(userId), get_game_title(gameId) FROM rating WHERE userId='{userId}';")
    elif (gameId is not None):
        cursor.execute(f"SELECT ratingValue, ratingDescription, get_user_name(userId), get_game_title(gameId) FROM rating WHERE gameId='{gameId}';")
    else:
        cursor.execute("SELECT ratingValue, ratingDescription, get_user_name(userId), get_game_title(gameId) FROM rating;")
    # Create and print the pretty table of games
    pt = from_db_cursor(cursor)
    pt.field_names = ["Rating (0 - 10)", "Description", "User", "Game"]
    pt.align["Rating (0 - 10)"] = "l"
    pt.align["Description"] = "l"
    pt.align["User"] = "l"
    pt.align["Game"] = "l"
    pt.sortby = "Game"
    print(pt)