#from pickle import FALSE, NONE <-- I dont know what this is
#from types import NoneType    <-- or this
from manage_games import list_games
import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

#conneciton to the database
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")


def manage_playthroughs(userId):

    # While the user still wants to do something here
    done = False
    while (not done):
        # Ask whether the user would like to view playthroughs, or edit them
        #dump all avaliable playthrough to the user
        listPT(userId, None, 0)
        userInput = None
        while (userInput != 'S' and userInput != 'E' and userInput != 'B' and userInput != 'A'  and userInput != 'R' ):
            userInput = input("Enter:\n[S]-Search\n[E]-Edit\n[A]-add\n[R]-reports\n[B]-Back")
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
    userInput = None
    while userInput != 'C' and userInput != 'G':
        userInput = input("Enter for report on: \n[C]-completed Games\n[G]-most played Genre")
    if userInput == 'C':
        ReportPTComp(userID)
    elif userInput == 'G':
        ReportPTGen()


def searchPT(userId):
    userInput = None
    while (userInput != 'N' and userInput != 'G'):
        userInput = input("Enter to search by: \n[N]-name\n[G]-game") 
    if userInput == 'N':
        searchPTName(userId)
    elif userInput == 'G':
        searchPTGame(userId)




def searchPTName(userId):
    userInput = input("Enter the Name of the playthrough you are searching for: ")
    listPT(userId, userInput, 1)

def searchPTGame(userId):
    userInput = input("Enter the Game title for the Playthroughs you are searching for: ")
    listPT(userId, userInput, 2)


def ReportPTGen():
    None


def ReportPTComp(userId):
    userInput = None
    listPT(userId, userInput, 3)

def addPT(userId):

    list_games(None, None, userId, None)

    flag = False
    while flag == False:
        gameId = ("Select the GameID you wish to create a playthrough for")
        cursor.execute("SELECT * from game where gameid='{gameId}'")
        result = cursor.fetchone()
        if result == None:
            flag = True

    flag = False
    while flag == False:
        addPTName = input("Enter the new name of the playthrough you want to add: ")
        cursor.execute("SELECT * from Playthrough where playthroughName='{addPTName}'")
        result = cursor.fetchone()
        if result == None:
            flag = True

    flag = False
    addPTDesc = input("Enter the Description of the playthrough you are adding: ")

    addPTTarg = input("Enter the target percentage of this playthrough: ")

    cursor.execute(f"INSERT INTO Playthrough (PlaythroughName, playthroughDescription, GameId, userId) VALUES ('{addPTName}','{addPTDesc}','{gameId}','{userId}');")
    conn.commit()
    

def editPT(userID):
    listPT(userID, None, 0)
    flag = None
    while flag == False:
        ptId = input("Which playthrough do you wish to edit (Insert Playthrough ID): ")
        cursor.execute("SELECT * from Playthrough where playthroughID='{PTId}'")
        result = cursor.fetchone()
        if result == None:
            flag = True
    userInput = input("Which column do you wish to edit: \n[N]-name\n[D]-Description\n[T]-Target percent\n[C]-Current percent\n[E]-End date")
    listPT(userID, ptId, 1)
    if userInput == 'N':
        userInput = input("what do you want the name to be")
        cursor.execute("Update playthrough set playthroughName = '{userinput}' where playthroughID = '{ptId}' ")
    elif userInput == 'D':
        userInput = input("what do you want the Description to be")
        cursor.execute("Update playthrough set playthroughDescription = '{userinput}' where playthroughID = '{ptId}' ")
    elif userInput == 'T':
        userInput = input("what do you want the Target Percent to be")
        cursor.execute("Update playthrough set playthroughTargetPercent = '{userinput}' where playthroughID = '{ptId}' ")
    elif userInput == 'C':
        userInput = input("what do you want the current percent to be")
        cursor.execute("Update playthrough set playthroughCurrent Percent = '{userinput}' where playthroughID = '{ptId}' ")
    elif userInput == 'E':
        userInput = input("what do you want the End date to be")
        cursor.execute("Update playthrough set playthroughEndDate = '{userinput}' where playthroughID = '{ptId}' ")


""" If userId is specified then only list playthroughs for that user """
'''mode is the type of value for the second input 
0 - userID was passed
1 - playthrough name was passed
2 - gamename was passed
3 - completed games have been passed
'''
def listPT(userId, inputstr, mode):
    # Execute the query to get the playthroughs list
    cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}';")
    # Check if we only want to list playthroughs for a specific user
    if (mode == 0):
        cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}';")
    elif (mode == 1):
        cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}' and playthroughName='{inputstr}';")
    elif (mode == 2):
        cursor.execute(f"SELECT gameID FROM Game WHERE userId={userId} and gameTitle='{inputstr}'")
        result = cursor.fetchone()
        '''if (result == None):
                print(f"{gameTitle} does not exist!")
                gameTitle = None
                return'''
        cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}' and gameId='{result}';")
    elif (mode == 3):
        cursor.execute(f"Call GetCompleted('{userId}')")
    else:
        cursor.execute("SELECT * FROM playthrough;")
    # Create and print the pretty table of playthroughs
    pt = from_db_cursor(cursor)
    pt.field_names = ["Playthrough ID", "Name", "Description", "Target %", "Current %", "Started On", "Completed On", "Game ID", "User ID"]
    pt.del_column("Playthrough ID")
    pt.align["Name"] = "l"
    pt.align["Description"] = "l"
    pt.align["Target %"] = "l"
    pt.align["Current %"] = "l"
    pt.align["Started On"] = "l"
    pt.align["Completed On"] = "l"
    pt.del_column("Game ID")
    pt.del_column("User ID")
    pt.sortby = "Name"
    print(pt)
