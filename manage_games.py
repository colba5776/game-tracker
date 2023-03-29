import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

# Establish a connection, create a cursor and set it to use gametrackerdb
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

def manage_games(userId):
    # List out all the games in the database
    list_games(None)
    # While the user still wants to do something here
    done = False
    while (not done):
        # Ask whether the user would like to view games, or edit them
        userInput = None
        while (userInput != 'S' and userInput != 'E' and userInput != 'B'):
            userInput = input("Enter [S] to Search, [E] to Edit or Add, [B] to go Back: ")

        # If they wish to search for a game
        if (userInput == 'S'):
            # Display list of all games
            list_games(None) # DO SOMETHING ELSE HERE
        # If they wish to edit a game
        if (userInput == 'E'):
            edit_game(userId)
        # If they wish to leave
        if (userInput == 'B'):
            done = True

""" Used to add a new game to the database """ 
def edit_game(ownerId):
    # Ask whether the user would like to add a game, or update one
    userInput = None
    while (userInput != 'A' and userInput != 'U'):
        userInput = input("Enter [A] to Add a game, [U] to Update a game: ")
    
    # If the user wants to add a new game
    if (userInput == 'A'):
        # Ask user for the name of their game
        print("Please enter the following information on the game you wish to add: ")
        # Make sure the game's title does not already exist in the databse (used to prevent duplicate names)
        gameTitle = None
        while (gameTitle == None):
            gameTitle = input("Title: ")
            # Check name availability
            cursor.execute(f"SELECT gameTitle FROM game WHERE gameTitle='{gameTitle}';")
            result = cursor.fetchone() # Get the resulting row for the query
            if (result is not None):
                print(f"{gameTitle} has already been added!")
                gameTitle = None
        # Get game's description
        gameDescription = input("Description: ")
        # List all available genres and ask the user to choose one of them
        gameGenre = None
        while (gameGenre == None):
            list_genres()
            gameGenre = input("Genre: ")
            # Check if the genre is valid
            genreId = None
            cursor.execute(f"SELECT genreId FROM genre WHERE genreName='{gameGenre}';")
            result = cursor.fetchone() # Get the resulting row for the query
            if (result is None):
                print(f"{gameGenre} is not a valid genre!")
                gameGenre = None
            else:
                genreId = result[0]
        # Insert the game into the database, notify the user, and ask them if they would like to add any achievements as well
        cursor.execute(f"INSERT INTO game (gameTitle, gameDescription, genreId, userId) VALUES ('{gameTitle}','{gameDescription}','{genreId}','{ownerId}');")
        conn.commit()
        # Get and store the gameId of the new game
        result = cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}'")
        gameId = result[0]
        userInput = None
        while (userInput != 'Y' and userInput != 'N'):
            userInput = input(f"{gameTitle} successfully added!\n Would you like to add any achievements for this game?\nEnter [Y] for Yes, [N] for No: ")
        # If they want to add achievements
        if (userInput == 'Y'):
            add_achievements(gameId, ownerId)

""" Used to allow user to insert new achievements into the database """
def add_achievements(gameId):
    done = False
    """while (not done):
        Implement Achievement Insertion here!"""

""" Used to list out all the games in the database """
""" If ownerId is not None, then only list games added by ownerId """
def list_games(ownerId):
    # Check if we only want to list games added by ownerId
    if (ownerId is not None):
        cursor.execute(f"SELECT * FROM game WHERE userId='{ownerId}';")
    else:
        cursor.execute("SELECT * FROM game;")
    # Create and print the pretty table of games
    pt = from_db_cursor(cursor)
    pt.field_names = ["Game ID", "Title", "Description", "Genre", "Owner"]
    pt.del_column("Game ID")
    pt.align["Title"] = "l"
    pt.del_column("Description")
    pt.align["Genre"] = "l"
    pt.align["Owner"] = "l"
    pt.sortby = "Title"
    print(pt)

""" Used to list out all the genres in the database """
def list_genres():
    cursor.execute("SELECT * FROM genre;")
    # Create and print the pretty table of genres
    pt = from_db_cursor(cursor)
    pt.field_names = ["ID", "Genres", "Description"]
    pt.del_column("ID")
    pt.align["Genres"] = "l"
    pt.del_column("Description")
    pt.sortby = "Genres"
    print(pt)

