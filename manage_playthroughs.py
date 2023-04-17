#from pickle import FALSE, NONE <-- I dont know what this is
#from types import NoneType    <-- or this
from manage_games import list_games
import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect
from manage_games import list_achievements

#conneciton to the database
conn = connect()
cursor = conn.cursor(buffered=True)
cursor.execute("USE gametrackerdb;")

def manage_playthroughs(userId):
    # While the user still wants to do something here
    listPT(userId, None, -1)
    done = False
    while (not done):
        # Ask whether the user would like to view playthroughs, or edit them
        #dump all avaliable playthrough to the user
        userInput = None
        while (userInput != 'S' and userInput != 'E' and userInput != 'B' and userInput != 'A'  and userInput != 'R' ):
            userInput = input("Enter [S] to Search, [E] to Edit, [A] to Add, [R] for Reports, [B] to go Back: ")
        # If they wish to search for a playthrough
        if (userInput == 'S'):
            searchPT(userId)
        # If they wish to edit a playthrough
        elif (userInput == 'E'):
            editPT(userId)
        # If they wish to add a playthrough
        elif (userInput == 'A'):
            addPT(userId)
        elif (userInput == 'R'):
            reports(userId)
        # If they wish to leave
        elif (userInput == 'B'):
            done = True
        userInput = None

def reports(userID):
    # ReportPTGen()
    userInput = None
    while userInput != 'C' and userInput != 'V':
        userInput = input("Enter [V] to View a specific playthrough, [C] to View completed playthroughs: ")
    if userInput == 'C':
        ReportPTComp(userID)
    elif userInput == 'V':
        ReportPTView(userID)
    
def searchPT(userId):
    userInput = None
    while (userInput != 'N' and userInput != 'G'):
        userInput = input("Enter [N] to search for specific Playthrough by Name, User, and Game, [G] to search by Game Title: ") 
    if userInput == 'N':
        searchPTName(userId)
    elif userInput == 'G':
        searchPTGame(userId)

def searchPTName(userId):
    # Get the userId
    searchByUserId = None
    while searchByUserId is None:
        userName = input("Enter the user name you would like to search by: ")
        # Get the userId
        cursor.execute(f"SELECT userId FROM user WHERE userName='{userName}';")
        result = cursor.fetchone()
        if (result is None):
            print(f"User {userName} does not exist.")
        else:
            searchByUserId = result[0]
            # Check if any playthroughs actually exist
            cursor.execute(f"SELECT * FROM playthrough WHERE userId='{searchByUserId}';")
            result = cursor.fetchone()
            if (result[0] is None):
                print(f"No playthroughs exist for user '{userName}'")
                return
            # List out playthroughs that userId matches to
            print(f"----- Playthroughs for user {userName} -----")
            listPT(searchByUserId, None, 0)
    # Ask the user which game the playthrough is for
    gameId = None
    while (gameId== None):
        gameTitle = input("Enter the game you would like to search by: ")
        # Check if the game exists
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"{gameTitle} does not exist.")
        else:
            gameId = result[0]
            # Check if any playthroughs actually exist
            cursor.execute(f"SELECT * FROM playthrough WHERE userId='{searchByUserId}' AND gameId='{gameId}';")
            result = cursor.fetchone()
            if (result[0] is None):
                print(f"No playthroughs on game '{gameTitle}' exist for this user.")
                gameId = None
                return
            # List out playthroughs that userId and gameId matches to
            print(f"----- Playthroughs for this user on game {gameTitle} -----")
            listPT(searchByUserId, gameTitle, 2)
    # Ask the user which playthrough they would like to view information on
    playthroughId = None
    while (playthroughId == None):
        # Ask them which playthroughName they would like to search for
        playthroughName = input("Enter the playthrough name you would like to search by: ")
        # Check if the playthrough exists
        cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{playthroughName}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"Playthrough {playthroughName} does not exist!")
        else:
            # Check if the provided playthrough actually exists
            cursor.execute(f"SELECT playthroughId FROM playthrough WHERE userId='{searchByUserId}' AND gameId='{gameId}' AND playthroughName='{playthroughName}';")
            result = cursor.fetchone()
            playthroughId = result[0]
            if (result[0] is None):
                print(f"No playthrough with name '{playthroughName}' exist for this user on this game.")
                return
            # Find and list the playthrough
            listPT(searchByUserId, playthroughId, 5)

def searchPTGame(userId):
    # Ask whether the user which playthrough they would like to view information on
    gameTitle = None
    while (gameTitle == None):
        gameTitle = input("Enter the game you would like to search by: ")
        # Check if the playthrough exists
        cursor.execute(f"SELECT gameTitle FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"No playthrough exists for {gameTitle}.")
            gameTitle = None
    listPT(userId, gameTitle, 4)

def ReportPTGen():
    print("Your playthrough statistics: ")
    None

def ReportPTComp(userId):
    userInput = None
    listPT(userId, userInput, 3)

def ReportPTView(userId):
    # Ask the user which game the playthrough is for
    gameId = None
    while (gameId== None):
        gameTitle = input("Enter the game you would like to search by: ")
        # Check if the game exists
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"{gameTitle} does not exist.")
        else:
            gameId = result[0]
            # Check if any playthroughs actually exist
            cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}' AND gameId='{gameId}';")
            result = cursor.fetchone()
            if result is None:
                print(f"No playthroughs on game '{gameTitle}' exist for this user.")
                gameId = None
                return
            # List out playthroughs that userId and gameId matches to
            print(f"----- Your playthroughs for {gameTitle} -----")
            listPT(userId, gameTitle, 2)
    # Ask the user which playthrough they would like to view information on
    playthroughId = None
    while (playthroughId == None):
        # Ask them which playthroughName they would like to search for
        playthroughName = input("Enter the playthrough name you would like to search by: ")
        # Check if the playthrough exists
        cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{playthroughName}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"Playthrough {playthroughName} does not exist!")
        else:
            # Check if the provided playthrough actually exists
            cursor.execute(f"SELECT playthroughId FROM playthrough WHERE userId='{userId}' AND gameId='{gameId}' AND playthroughName='{playthroughName}';")
            result = cursor.fetchone()
            playthroughId = result[0]
            if result is None:
                print(f"No playthrough with name '{playthroughName}' exist for this user on this game.")
                return
    # List playthrough information
    listPT(userId, playthroughId, 1)
    # Check if there are any achievements in this playthrough
    cursor.execute(f"SELECT achievementId FROM playthroughachievement WHERE playthroughId='{playthroughId}';")
    result = cursor.fetchone()
    if result is not None:
        # Ask them if they would like to view the achievements for this playthrough
        userInput = None
        while (userInput != 'Y' and userInput != 'N'):
            userInput = input("Would you like to view achievements for this playthrough? Enter [Y] for Yes, [N] for No: ")
        # Display the playthrough achievement list for this playthrough if the user says yes
        if (userInput == 'Y'):
            list_playthrough_achievements(playthroughId, True)
    else:
        print("This playthrough does not include any achievements.")

def addPT(userId):
    list_games(None, None, None, None)
    gameId = None
    while (gameId == None):
        # Ask them for the name of the game they wish to create a new playthrough for
        gameTitle = input("Enter the title of the game you would like to create a playthrough for: ")
        # Get gameId
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone() # Get the resulting row for the query
        gameId = result[0]
        # Check if the game exists
        if (gameId is None):
            print(f"{gameTitle} does not exist.")
            gameId = None
    # Get the name for the new playthrough and make sure it is unique
    addPTName = None
    while addPTName is None:
        addPTName = input("Enter the new name of the playthrough you want to add: ")
        # Check if this name is already in use for this game by this user
        cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{addPTName}' AND userId='{userId}' AND gameId='{gameId}';")
        result = cursor.fetchone()
        if result is not None:
            print(f"You already have a playthrough named '{addPTName}' for this game!")
            addPTName = None
    # Get the description for the new playthrough
    addPTDesc = input("Enter the Description of the playthrough you are adding: ")
    # Get the target percent for the new playthrough
    addPTTarg = input("Enter the target percentage of this playthrough (Enter [NA] if not applicable): ")
    if (addPTTarg == 'NA'):
        cursor.execute(f"INSERT INTO playthrough (playthroughName, playthroughDescription, gameId, userId) VALUES ('{addPTName}','{addPTDesc}','{gameId}','{userId}');")
    else:
        cursor.execute(f"INSERT INTO playthrough (playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, gameId, userId) VALUES ('{addPTName}','{addPTDesc}','{addPTTarg}', 0,'{gameId}','{userId}');")
    conn.commit()
    # Get the new playthrough's Id
    cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{addPTName}' AND gameId='{gameId}' AND userId='{userId}';")
    result = cursor.fetchone()
    playthroughId = result[0]
    # List the new playthrough
    print(f"{addPTName} successfully created!")
    listPT(userId, playthroughId, 5)
    # Ask if they would like to add any achievements for it
    userInput = None
    while (userInput != 'Y' and userInput != 'N'):
        userInput = input("Would you like to add any achievements to this playthrough?\nEnter [Y] for Yes, [N] for No: ")
    # If they want to add achievements
    if (userInput == 'Y'):
        add_playthrough_achievements(playthroughId, gameId)

""" Used to allow user to insert new achievements into the database """
def add_playthrough_achievements(playthroughId, gameId):
    # Print out list of available achievements
    print("----- Available achievements for this game -----")
    list_achievements(gameId)
    done = False
    while (not done):
        # Get the achievementId and make sure it is valid
        validAchievement = True
        achievementId = None
        while achievementId == None:
            # Get achievement name
            achievementName = input("Achievement name: ")
            cursor.execute(f"SELECT achievementId FROM achievement WHERE achievementName='{achievementName}' AND gameId='{gameId}';")
            result = cursor.fetchone()
            if result is None:
                print(f"Achievement {achievementName} does not exist for this game.")
            else:
                achievementId = result[0]
                # Check if this achievement is already present in the playthrough
                cursor.execute(f"SELECT * FROM playthroughachievement WHERE achievementId='{achievementId}';")
                result = cursor.fetchone()
                if result is not None:
                    print(f"Achievement with name {achievementName} has already been added to this playthrough!")
                    validAchievement = False
        # Insert the new achievement into the database if it is valid
        if (validAchievement):
            cursor.execute(f"INSERT INTO playthroughachievement (achievementStatus, achievementId, playthroughId) VALUES ('Incomplete','{achievementId}','{playthroughId}');")
            conn.commit()
        # Print out list of achievements for this game
        print(f"----- Current achievements for this playthrough -----")
        list_playthrough_achievements(playthroughId, False)
        # Ask user if they would still like to add an achievement and set done to True if they say No
        userInput = None
        while (userInput != 'Y' and userInput != 'N'):
            userInput = input("Add another achievement? Enter [Y] for Yes, [N] for No: ")
        if (userInput == 'N'):
            done = True

def editPT(userID):
    print("----- Your playthroughs -----")
    listPT(userID, None, 0)
    # Ask the user which game the playthrough is for
    gameId = None
    while (gameId== None):
        gameTitle = input("Enter the game you would like to search by: ")
        # Check if the game exists
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{gameTitle}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"{gameTitle} does not exist.")
        else:
            gameId = result[0]
            # Check if any playthroughs actually exist
            cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userID}' AND gameId='{gameId}';")
            result = cursor.fetchone()
            if result is None:
                print(f"No playthroughs on game '{gameTitle}' exist for this user.")
                gameId = None
                return
            # List out playthroughs that userId and gameId matches to
            print(f"----- Your playthroughs for {gameTitle} -----")
            listPT(userID, gameTitle, 2)
    # Ask the user which playthrough they would like to view information on
    ptId = None
    while (ptId == None):
        # Ask them which playthroughName they would like to search for
        playthroughName = input("Enter the playthrough name you would like to search by: ")
        # Check if the playthrough exists
        cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{playthroughName}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"Playthrough {playthroughName} does not exist!")
        else:
            # Check if the provided playthrough actually exists
            cursor.execute(f"SELECT playthroughId FROM playthrough WHERE userId='{userID}' AND gameId='{gameId}' AND playthroughName='{playthroughName}';")
            result = cursor.fetchone()
            ptId = result[0]
            if result is None:
                print(f"No playthrough with name '{playthroughName}' exist for this user on this game.")
                return
    # Let the user keep making edits until they wish to stop
    done = False
    while not done:
        print("----- The playthrough you selected -----")
        listPT(userID, ptId, 1)
        userInput = input("What would you like to edit? Enter:\n[N] for Name\n[D] for Description\n[T] for Target percent\n[A] for Achievements status\n[C] for Current percent\n[Complete] to Complete the playthrough or update the completion date to today's date\n[Done] when you are Done\n")
        if userInput == 'N':
            userInput = input("What do you want the name to be: ")
            cursor.execute(f"Update playthrough set playthroughName='{userInput}' where playthroughId='{ptId}';")
            conn.commit()
            print(f"Playthrough name changed to - {userInput}")
        elif userInput == 'D':
            userInput = input("What do you want the Description to be: ")
            cursor.execute(f"Update playthrough set playthroughDescription='{userInput}' where playthroughId='{ptId}';")
            conn.commit()
            print(f"Playthrough description changed to - {userInput}")
        elif userInput == 'T':
            # Get the target percent for the new playthrough
            userInput = input("Enter the new target percentage of this playthrough (Enter [NA] if no longer applicable): ")
            if (userInput == 'NA'):
                cursor.execute(f"Update playthrough set playthroughTargetPercent=NULL where playthroughId='{ptId}';")
                cursor.execute(f"Update playthrough set playthroughCurrentPercent=NULL where playthroughId='{ptId}';")
            else:
                cursor.execute(f"Update playthrough set playthroughTargetPercent='{userInput}' where playthroughId='{ptId}';")
            conn.commit()
            print(f"Playthrough target percent changed to - {userInput}%")
        elif userInput == 'C':
            # Check if targetPercent is null
            cursor.execute(f"SELECT playthroughTargetPercent FROM playthrough WHERE playthroughId='{ptId}';")
            result = cursor.fetchone()
            if result is None:
                print("This playthrough's target percent is set not applicable! Please change the target percent first.")
                return
            userInput = input("What do you want the current percent to be: ")
            cursor.execute(f"Update playthrough set playthroughCurrentPercent='{userInput}' where playthroughId='{ptId}';")
            conn.commit()
            print(f"Playthrough current percent changed to - {userInput}%")
        elif userInput == 'Complete':
            cursor.execute(f"Update playthrough set playthroughEndDate = CURDATE() where playthroughId = '{ptId}';")
            conn.commit()
            print(f"Playthrough end date updated to today.")
        elif userInput == 'A':
            print("----- List of achievements for this playthrough -----")
            list_playthrough_achievements(ptId, False)
            # Get the achievementId and make sure it is valid
            achievementId = None
            while achievementId == None:
                # Get achievement name
                achievementName = input("Enter the name of achievement would you like to toggle completion status for (Complete/Incomplete): ")
                cursor.execute(f"SELECT achievementId FROM achievement NATURAL JOIN playthroughachievement WHERE achievementName='{achievementName}' AND playthroughId='{ptId}';")
                result = cursor.fetchone()
                if result is None:
                    print(f"Achievement {achievementName} does not exist for this game.")
                else:
                    achievementId = result[0]
            # The new value we want to set the status to
            newStatus = ''
            cursor.execute(f"SELECT achievementStatus FROM playthroughachievement WHERE achievementId='{achievementId}' AND playthroughId='{ptId}';")
            result = cursor.fetchone()
            if (result[0] == 'Incomplete'):
                newStatus = "Complete"
            else:
                newStatus = "Incomplete"
            # Set the new status
            cursor.execute(f"UPDATE playthroughachievement SET achievementStatus='{newStatus}' WHERE playthroughId='{ptId}' AND achievementId='{achievementId}';")
            conn.commit()
            print(f"Achievement status updated to {newStatus}.")
        elif userInput == 'Done':
            done = True

""" If userId is specified then only list playthroughs for that user """
'''mode is the type of value for the second input 
0 - userID was passed
1 - playthrough name was passed
2 - gamename was passed
3 - completed games have been passed
'''
def listPT(userId, inputstr, mode):
    # Execute the query to get the playthroughs list
    # cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}';")
    # Check if we only want to list playthroughs for a specific user
    if (mode == 0):
        cursor.execute(f"SELECT playthroughId, playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, playthroughStartDate, playthroughEndDate, get_game_title(gameId), get_user_name(userId) FROM playthrough WHERE userId='{userId}';")
    elif (mode == 1):
        cursor.execute(f"SELECT playthroughId, playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, playthroughStartDate, playthroughEndDate, get_game_title(gameId), get_user_name(userId) FROM playthrough WHERE userId='{userId}' and playthroughId='{inputstr}';")
    elif (mode == 2):
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{inputstr}';")
        result = cursor.fetchone()
        gameId = result[0]
        '''if (result == None):
                print(f"{gameTitle} does not exist!")
                gameTitle = None
                return'''
        cursor.execute(f"SELECT playthroughId, playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, playthroughStartDate, playthroughEndDate, get_game_title(gameId), get_user_name(userId) FROM playthrough WHERE userId='{userId}' and gameId='{gameId}';")
    elif (mode == 3):
        cursor.execute(f"SELECT playthroughId, playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, playthroughStartDate, playthroughEndDate, get_game_title(gameId), get_user_name(userId) FROM playthrough WHERE playthroughEndDate IS NOT NULL and userId='{userId}';")
    elif (mode == 4):
        cursor.execute(f"SELECT gameId FROM game WHERE gameTitle='{inputstr}';")
        result = cursor.fetchone()
        gameId = result[0]
        cursor.execute(f"SELECT playthroughId, playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, playthroughStartDate, playthroughEndDate, get_game_title(gameId), get_user_name(userId) FROM playthrough WHERE gameId='{gameId}';")
    elif (mode == 5):
        cursor.execute(f"SELECT playthroughId, playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, playthroughStartDate, playthroughEndDate, get_game_title(gameId), get_user_name(userId) FROM playthrough WHERE playthroughId='{inputstr}';")
    else:
        cursor.execute("SELECT playthroughId, playthroughName, playthroughDescription, playthroughTargetPercent, playthroughCurrentPercent, playthroughStartDate, playthroughEndDate, get_game_title(gameId), get_user_name(userId) FROM playthrough;")
    # Create and print the pretty table of playthroughs
    pt = from_db_cursor(cursor)
    pt.field_names = ["Playthrough ID", "Name", "Description", "Target %", "Current %", "Started On", "Completed On", "Game", "User"]
    pt.del_column("Playthrough ID")
    pt.align["Name"] = "l"
    pt.align["Description"] = "l"
    pt.align["Target %"] = "l"
    pt.align["Current %"] = "l"
    pt.align["Started On"] = "l"
    pt.align["Completed On"] = "l"
    pt.align["Game"] = "l"
    pt.align["User"] = "l"
    pt.sortby = "Name"
    print(pt)

""" Used to list out all the achievements in the database """
""" If gameId is not None, then only list achievements for the provided game """
def list_playthrough_achievements(playthroughId, listStats):
    # Check if we want to list completed percentage
    if listStats is True:
        cursor.execute(f"SELECT get_achievement_completed_percent('{playthroughId}');")
        result = cursor.fetchone()
        completedAchievementsPercent = result[0]
        print(f"You have completed {completedAchievementsPercent}% of the achievements.")
    # Get the list of achievements
    cursor.execute(f"SELECT achievementStatus, get_achievement_name(achievementId) FROM playthroughachievement WHERE playthroughId='{playthroughId}';")
    # Create and print the pretty table of achievements
    pt = from_db_cursor(cursor)
    pt.field_names = ["Status", "Name"]
    pt.align["Status"] = "l"
    pt.align["Name"] = "l"
    pt.sortby = "Status"
    print(pt)