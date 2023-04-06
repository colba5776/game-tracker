import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

# Establish a connection, create a cursor and set it to use gametrackerdb
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

def manage_games(userId):
    # List out all the games in the database
    list_games(None, None)
    # While the user still wants to do something here
    done = False
    while (not done):
        # Ask whether the user would like to view games, or edit them
        userInput = None
        while (userInput != 'S' and userInput != 'E' and userInput != 'V' and userInput != 'B'):
            userInput = input("Enter [S] to Search, [V] to View, [E] to Edit or Add, [B] to go Back: ")

        # If they wish to search for a game
        if (userInput == 'S'):
            # Display list of all games
            list_games(None, None) # DO SOMETHING ELSE HERE
        # If they wish to view info on a game
        if (userInput == 'V'):
            view_game()
        # If they wish to edit a game
        if (userInput == 'E'):
            edit_game(userId)
        # If they wish to leave
        if (userInput == 'B'):
            done = True

""" Used to allow the user to view different game's information """
def view_game():
    # Ask whether the user which game they would like to view information on
    gameTitle = None
    while (gameTitle == None):
        gameTitle = input("Enter the title for the game you would like to view: ")
        # Check if the game exists
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"{gameTitle} does not exist!")
            gameTitle = None
    # Get and store the gameId of the new game
    result = cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
    result = cursor.fetchone()
    gameId = result[0]
    # List game information
    list_games(None, gameId)
    # Ask them if they would like to view the achievements for this game
    userInput = None
    while (userInput != 'Y' and userInput != 'N'):
        userInput = input("Would you like to view achievements for this game? Enter [Y] for Yes, [N] for No: ")
    # Display the achievement list for this game if the user says yes
    if (userInput == 'Y'):
        list_achievements(gameId)

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
        result = cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone()
        gameId = result[0]
        userInput = None
        while (userInput != 'Y' and userInput != 'N'):
            userInput = input(f"{gameTitle} successfully added!\nWould you like to add any achievements for this game?\nEnter [Y] for Yes, [N] for No: ")
        # If they want to add achievements
        if (userInput == 'Y'):
            add_achievements(gameId)
        # Here is your newly added game!

    # If the user entered U to update a game
    else:
        # Check if they own any games and cancel if they do not
        cursor.execute(f"SELECT * FROM game WHERE userId='{ownerId}';")
        result = cursor.fetchone()
        if (result is None):
            print("You have not added any games!")
            return
        # Print out the list of games the user can Update (only games that they added themselves)
        print("----- Your Games -----")
        list_games(ownerId, None)
        # Make sure the game's title matches the title of a game this user owns
        gameTitle = None
        while (gameTitle == None):
            # Ask them for the name of the game they wish to update
            gameTitle = input("Enter the title of the game you would like to update: ")
            # Check if they own the game
            cursor.execute(f"SELECT gameTitle FROM game WHERE gameTitle='{gameTitle}' AND userId='{ownerId}';")
            result = cursor.fetchone() # Get the resulting row for the query
            if (result is None):
                print(f"{gameTitle} is not in the list of games you've added.")
                gameTitle = None
        # Get and store the gameId of the game they wish to update
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone()
        gameId = result[0]
        # Ask them what they would like to update
        userInput = None
        if (userInput != 'T' and userInput != 'D' and userInput != 'G'):
            userInput = input(f"What would you like to update for {gameTitle}?\nEnter [T] for Title, [D] for Description, or [G] for Genre: ")
        # Let the user update the title
        if (userInput == 'T'):
            # Make sure the game's newTitle does not already exist in the databse (used to prevent duplicate names)
            newTitle = None
            while (newTitle == None):
                newTitle = input(f"Enter your new title for {gameTitle}: ")
                # Check name availability
                cursor.execute(f"SELECT gameTitle FROM game WHERE gameTitle='{newTitle}' AND gameId!='{gameId}';")
                result = cursor.fetchone() # Get the resulting row for the query
                if (result is not None):
                    print(f"{newTitle} already exists!")
                    gameTitle = None
            # Update the game's title to newTitle
            cursor.execute(f"UPDATE game SET gameTitle='{newTitle}' WHERE gameId='{gameId}';")
            conn.commit()
            print("Title updated!")
        # Let the user update the description
        if (userInput == 'D'):
            # Get game's description
            newDescription = input(f"Enter the new description for {gameTitle}: ")
            # Update the game's description
            cursor.execute(f"UPDATE game SET gameDescription='{newDescription}' WHERE gameId='{gameId}';")
            conn.commit()
            print("Description updated!")
        # Let the user update the genre
        if (userInput == 'G'):
            # List all available genres and ask the user to choose one of them
            newGenre = None
            while (newGenre == None):
                list_genres()
                newGenre = input(f"Enter your new genre for {gameTitle}: ")
                # Check if the genre is valid
                genreId = None
                cursor.execute(f"SELECT genreId FROM genre WHERE genreName='{newGenre}';")
                result = cursor.fetchone() # Get the resulting row for the query
                if (result is None):
                    print(f"{newGenre} is not a valid genre!")
                    newGenre = None
                else:
                    genreId = result[0]
            # Update the game's genre
            cursor.execute(f"UPDATE game SET genreId='{genreId}' WHERE gameId='{gameId}';")
            conn.commit()
            print("Genre updated!")

""" Used to allow user to insert new achievements into the database """
def add_achievements(gameId):
    done = False
    while (not done):
        # Get achievement name
        achievementName = input("Name: ")
        # Get achievement description
        achievementDescription = input("Description: ")
        # Check if the information looks good
        userInput = None
        while (userInput != 'Y' and userInput != 'N'):
            userInput = input("Does this information looks correct? Enter [Y] to Confirm, [N] to Cancel: ")
        if (userInput == 'Y'):
            # Insert the new achievement into the database
            cursor.execute(f"INSERT INTO achievement (achievementName, achievementDescription, gameId) VALUES ('{achievementName}','{achievementDescription}','{gameId}');")
            conn.commit()
            # Print out list of achievements for this game
            print(f"----- Achievement list -----")
            list_achievements(gameId)
        # Ask user if they would still like to add an achievement and set done to True if they say No
        userInput = None
        while (userInput != 'Y' and userInput != 'N'):
            userInput = input("Add another achievement? Enter [Y] for Yes, [N] for No: ")
        if (userInput == 'N'):
            done = True

""" Used to list out all the games in the database """
""" If ownerId is not None, then only list games added by ownerId """
""" If gameId is not None, then only list the game with gameId """
def list_games(ownerId, gameId):
    # Check if we want to list a specific game
    if (gameId is not None):
        cursor.execute(f"SELECT gameID, gameTitle, gameDescription, get_genre_name(genreId), get_user_name(userId) FROM game WHERE gameId='{gameId}';")
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
        # Print the description for the game after the pretty table
        cursor.execute(f"SELECT gameDescription FROM game WHERE gameId='{gameId}';")
        result = cursor.fetchone()
        print(f"Description: {result[0]}\n")
    else:
        # Check if we only want to list games added by ownerId
        if (ownerId is not None):
            cursor.execute(f"SELECT gameID, gameTitle, gameDescription, get_genre_name(genreId), get_user_name(userId) FROM game WHERE userId='{ownerId}';")
        else:
            cursor.execute("SELECT gameID, gameTitle, gameDescription, get_genre_name(genreId), get_user_name(userId) FROM game;")
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

""" Used to list out all the achievements in the database """
""" If gameId is not None, then only list achievements for the provided game """
def list_achievements(gameId):
    # Check if we only want to list achivements for gameId
    if (gameId is not None):
        cursor.execute(f"SELECT * FROM achievement WHERE gameId='{gameId}';")
    else:
        cursor.execute("SELECT * FROM achievement;")
    # Create and print the pretty table of achievements
    pt = from_db_cursor(cursor)
    pt.field_names = ["Achievement ID", "Name", "Description", "Game ID"]
    pt.del_column("Achievement ID")
    pt.align["Name"] = "l"
    pt.align["Description"] = "l"
    pt.del_column("Game ID")
    pt.sortby = "Name"
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