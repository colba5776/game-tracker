
#Gregory Sylvester
#4/12/2023

import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

#conneciton to the database
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

LineD = "*======================================================*"

#change UserID when logining in 
globalUserID = null

#change gameID python script needed to choose which game
gameID = null

def main(userID):
        dumpPTTable(userID, null)
        globalUserID = userID
        leaveFlag = false
        while leaveflag == false:
                print(lineD)
                menuflag = input("What do you want to do \n[A]-add Playthrough \n[E]-edit Playthrough\n[S]-search playthrough\n[R]-Report Generation \n[e]-exit to previous Menu")
                match menuflag.lower():
                        case "a":
                                #Add dump game list and game id and have them choose a certian game from the presented list
                                print(lineD)
                                gameid = input("Enter the game id of which game you would like to add a playthrough for?: ")
                                addRun(userID, gameID)
                        case "b":
                                #add dump playthrough list and pT ID and have them choose a certain pt from the presented list
                                print(lineD)
                                PTID = input("Enter the playthrough ID of which playthrough you wish to edit")
                                editRUN(PTID)
                        case "c":
                                searchPT()
                        case "r":
                                reportGenPT()
                        case "e":
                                leaveflag = true
                        case _:
                                print(lineD)
                                print("Error: input value does not match any of the given choices please choose again")
                        
          print(lineD)
          
def reportGenPT():
        x= x +1
        
def SearchPT ():
        leaveflagSearchPT = false
        while leaveflagSearchPT == false:
                searchby = input("What do you want to Sort/search by:\n[a]-playthroughID\n[b]-playthrough name\n[c]-genre\n[E]-return to previous menu")
                match serchby.lower():
                        case "a":
                        case "b":
                        case "c":
                        case "e":
                                leaveflagsearchPT = true
                        case _: 
                                print(lineD)
                                print("Error: input value does not match any of the given choices please choose again")
        
def dumpPTTable(UserID, PTID):
	if pTID == null:
		cursor.execute(f"SELECT playthroughID, playthroughName, playthroughDesc, playthroughTargetpercent,playthroughCurrentpercent, playthroughstartdate, playthroughenddate from playthrough where userID = '{userID}' ")
	elif ptid != null && userid != null:
		cursor.execute(f"SELECT playthroughID, playthroughName, playthroughDesc, playthroughTargetpercent,playthroughCurrentpercent, playthroughstartdate, playthroughenddate from playthrough where userID = '{userID}', playthroughID = '{ptid}'")
        pt = from_db_cursor(cursor)
        print(pt)
        
#Used to create instance of playthrough
def addRun(insertUserID, insertGameID):

	#insert check funciton
	#already exists
	#limit varchar 45 add if statement on size
	#enter the playthrough description
	playthroughName = input("Enter your desired playthorugh name: ")
	while playthroughName > 45:
    	playthroughName = input("Enter your desired playthorugh name: ")

        #limit varchar 250 add if statement on size
        #enter the playthorugh description

        playthroughDescript = input("Enter playthrough description: ")
        while playthroughDescript > 250 :
                playthroughDescript = input("Enter playthrough description: ")

        #limit int percent should be less than 100
        #enter playthough target percentage
        playthroughTargetPercentage = input("Enter target percent for playthough: ")
        while playthroughTargetPercentage > 100:
                playthroughTargetPercentage = input("Enter target percent for playthough: ")

        #check to make sure the current percentage is forced to start at 0
        #enter playthorugh current percentage
        playthoughCurrentPerecntage = 0

        #insert statement may need to change with the curdate modifier        
        cursor.execute(f"INSERT INTO user (userID, gameID, playthoughName, playthroughDescription, playthoughTargetPercent) VALUES ('{insertUserID}', '{insertGameID}', '{playthroughName}','{playthroughDescript}', '{playthroughTargetPercentage}');")
        conn.commit()



def editRun(playthroughID):

	doneEdit = 'y'

	while doneEdit == 'y':

		changeValue = input("which attribute would you like to change?:\n[A]-Name \n[B]-playthroughDescription \n[C]-current percent\n[D]-target percent \n[E]-EndDate")

		#case on which value to change
		match changeValue.upper():
			case "A":
				editPlaythroughName(playthroughID)
			case "B":
				editPlaythroughDes(playthroughID)
			case "C":
				editPlaythroughPercent(playthroughID)
			case "D":
				editPlaythroughTargetPercent(playthroughID)
			case "E":
				editPlaythroughEndDate(playthroughID)
			case _:
				print("error: please enter a value A-E, input was not in this range")
		doneEdit = input(f"Do you want to change any other values on {playthroughID}: [y] - yes [n] - no")

def editPlaythroughName(playthroughID):
	editPlaythroughName = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")
	while len(editPlaythrougnName) >= 45:
		print("error the length of the string input is too long, please enter another name")
		editPlaythroughName = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")
	cursor.execute(f"call changePTNAME('{editPlaythroughName}','{playthroughID}')")
	conn.commit()


def editPlaythroughDes(playthroughID):
	editPlaythroughDesc = input("What would you like to change the description of the playthrough to(must be less than 45 characters)?: ")
	while len(editPlaythroughDesc) >= 250:
		print("error the length of the string input is too long, please enter another Description")
		editPlaythroughName = input("What would you like to change the Description of the playthrough to(must be less than 250 characters)?: ")
	cursor.execute(f"call changePTDESC('{editPlaythroughDESC}','{playthroughID}')")
	conn.commit()
	
def editPlaythroughPercent(playthroughID):
	editPlaythroughPerc = input("What is the percent playthrough (0-100)?: ")
	while editPlaythroughPerc > 100 && editPlaythroughPerc < 0:
		print("Error the value was not in range 0-100, please enter another Description")
		editPlaythroughPERC = input("What is the percent in the playthrough(must be 0-100)?: ")
	cursor.execute(f"call changePTPERC('{editPlaythroughPERC}','{playthroughID}')")
	conn.commit()

def editPlaythroughtargetPercent(playthroughID):
	editPlaythroughPercTarg = input("What is the percent playthrough Target(0-100)?: ")
	while editPlaythroughPercTarg > 100 & & editPlaythroughPercTarg < 0:
		print("Error the value was not in range 0-100, please enter another Description")
		editPlaythroughPERCTarg = input("What is the percent in the playthrough(must be 0-100)?: ")
	cursor.execute(f"call changePTPERCTarg('{editPlaythroughPERCTarg}','{playthroughID}')")
	conn.commit()

def editPlaythroughEndDate(playthroughID):

	#insert the update edit playthroughEnddate to be the curDate()
