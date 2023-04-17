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
            userInput = input("Enter:\n[S]-Search\n[E]-Edit\n[A]-Add\n[R]-Reports\n[B]-Back\n")
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
        userInput = input("Enter for report on: \n[V]-View a specific playthrough\n[C]-View completed\n")
    if userInput == 'C':
        ReportPTComp(userID)
    elif userInput == 'V':
        ReportPTView(userID)
    
def searchPT(userId):
    userInput = None
    while (userInput != 'N' and userInput != 'G'):
        userInput = input("Enter to search by: \n[N]-name\n[G]-game\n") 
    if userInput == 'N':
        searchPTName(userId)
    elif userInput == 'G':
        searchPTGame(userId)

def searchPTName(userId):
    # Ask whether the user which playthrough they would like to view information on
    playthroughId = None
    while (playthroughId == None):
        playthroughName = input("Enter the name you would like to search by: ")
        # Check if the playthrough exists
        cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{playthroughName}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"Playthrough {playthroughName} does not exist!")
        else:
            playthroughId = result[0]
    listPT(userId, playthroughId, 5)

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
    # Ask whether the user which playthrough they would like to view information on
    playthroughName = None
    while (playthroughName == None):
        playthroughName = input("Enter the name for the playthrough you would like to view: ")
        # Check if the playthrough exists
        cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{playthroughName}';")
        result = cursor.fetchone() # Get the resulting row for the query
        if (result is None):
            print(f"Playthrough {playthroughName} does not exist!")
            playthroughName = None
    # Get and store the playthroughId of the new game
    result = cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{playthroughName}';")
    result = cursor.fetchone()
    playthroughId = result[0]
    # List playthrough information
    listPT(userId, playthroughId, 1)
    # Ask them if they would like to view the achievements for this game
    userInput = None
    while (userInput != 'Y' and userInput != 'N'):
        userInput = input("Would you like to view achievements for this playthrough? Enter [Y] for Yes, [N] for No: ")
    # Display the playthrough achievement list for this playthrough if the user says yes
    if (userInput == 'Y'):
        list_playthrough_achievements(playthroughId, True)
    None

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

    flag = False
    while flag == False:
        addPTName = input("Enter the new name of the playthrough you want to add: ")
        cursor.execute(f"SELECT * from playthrough where playthroughName='{addPTName}'")
        result = cursor.fetchone()
        if result == None:
            flag = True

    flag = False
    addPTDesc = input("Enter the Description of the playthrough you are adding: ")

    addPTTarg = input("Enter the target percentage of this playthrough: ")

    cursor.execute(f"INSERT INTO playthrough (playthroughName, playthroughDescription, playthroughTargetPercent, gameId, userId) VALUES ('{addPTName}','{addPTDesc}','{addPTTarg}','{gameId}','{userId}');")
    conn.commit()
    cursor.execute(f"SELECT playthroughId FROM playthrough WHERE playthroughName='{addPTName}';")
    result = cursor.fetchone()
    playthroughId = result[0]
    userInput = None
    while (userInput != 'Y' and userInput != 'N'):
        userInput = input(f"{addPTName} successfully created!\nWould you like to add any achievements to this playthrough?\nEnter [Y] for Yes, [N] for No: ")
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
        # Insert the new achievement into the database
        cursor.execute(f"INSERT INTO playthroughachievement (achievementStatus, achievementId, playthroughId) VALUES ('Incomplete','{achievementId}','{playthroughId}');")
        conn.commit()
        # Print out list of achievements for this game
        print(f"----- Current achievement for this playthrough -----")
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
    ptId = None
    while ptId == None:
        playthroughName = input("Enter the name of the playthrough you wish to edit: ")
        cursor.execute(f"SELECT playthroughId from playthrough where playthroughName='{playthroughName}';")
        result = cursor.fetchone()
        if result == None:
            print(f"{playthroughName} does not exist.")
        else:
            ptId = result[0]

    print("----- The playthrough you selected -----")
    listPT(userID, ptId, 1)
    userInput = input("Which column do you wish to edit: \n[N]-name\n[D]-Description\n[T]-Target percent\n[A]-Achievements status\n[C]-Current percent\n[Complete]-Complete the playthrough or update the completion date to todays date\n")
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
        userInput = input("What do you want the Target Percent to be: ")
        cursor.execute(f"Update playthrough set playthroughTargetPercent='{userInput}' where playthroughId='{ptId}';")
        conn.commit()
        print(f"Playthrough target percent changed to - {userInput}%")
    elif userInput == 'C':
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