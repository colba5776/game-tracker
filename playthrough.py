
#Gregory Sylveser
#4/12/2023
#notes:
#merge with login_register or find another way to get userID and gameID
#values of Update statement and use of cursor
#insert protection for input of quotes or double quotes
#insert commit which insert the generated value

import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

#conneciton to the database
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

#change UserID when logining in 
userID = null

#change gameID python script needed to choose which game
gameID = null

def dumpPTTable(UserID, PTID):
	if pTID == null:
		cursor.execute(f"SELECT playthroughID, playthroughName, playthroughDesc, playthroughTargetpercent,playthroughCurrentpercent, playthroughstartdate, playthroughenddate from playthrough where userID = {userID} ")
	elif ptid != null and userid != null:
		cursor.execute(f"SELECT playthroughID, playthroughName, playthroughDesc, playthroughTargetpercent,playthroughCurrentpercent, playthroughstartdate, playthroughenddate from playthrough where userID = {userID}, playthroughID = {ptid}")

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

    #review insertion execution
    cursor.execute(f"INSERT INTO user (userID, gameID, playthoughName, playthroughDescription, playthoughTargetPercent) VALUES ('{insertUserID}', '{insertGameID}', '{playthroughName}','{playthroughDescript}', '{playthroughTargetPercentage}');")
    conn.commit()



def editRun(playthroughID):

	doneEdit = 'y'

	while doneEdit == 'y':

		changeValue = input("which attribute would you like to change?:\n[1] - Name \n[2] - playthroughDescription \n[3] - current percent\n[4] - target percent \n[5] - endDate")

		#case on which value to change
		match changeValue:
			case "1":
				editPlaythroughName(playthroughID)
			case "2":
				editPlaythroughDes(playthroughID)
			case "3":
				editPlaythroughPercent(playthroughID)
			case "4":
				editPlaythroughTargetPercent(playthroughID)
			case "5":
				editPlaythroughEndDate(playthroughID)
			case _:
				print("error: please enter a value 1-5, input was not in this range")
		doneEdit = input(f"Do you want to change any other values on {playthroughID}: [y] - yes [n] - no")

def editPlaythroughName(playthroughID):
	editPlaythroughName = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")
	while len(editPlaythrougnName) >= 45:
		print("error the length of the string input is too long, please enter another name")
		editPlaythroughName = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")
	cursor.execute(f"call changePTNAME(\""{editPlaythroughName}f",{playthroughID})")
	conn.commit()


def editPlaythroughDes(playthroughID):
	editPlaythroughDesc = input("What would you like to change the description of the playthrough to(must be less than 45 characters)?: ")
	while len(editPlaythroughDesc) >= 250:
		print("error the length of the string input is too long, please enter another Description")
		editPlaythroughName = input("What would you like to change the Description of the playthrough to(must be less than 250 characters)?: ")
	cursor.execute(f'call changePTDESC("{editPlaythroughDESC}",{playthroughID})')
	conn.commit()
	
def editPlaythroughPercent(playthroughID):
	editPlaythroughPerc = input("What is the percent playthrough (0-100)?: ")
	while editPlaythroughPerc > 100 and editPlaythroughPerc < 0:
		print("Error the value was not in range 0-100, please enter another Description")
		editPlaythroughPERC = input("What is the percent in the playthrough(must be 0-100)?: ")
	cursor.execute(f'call changePTPERC("{editPlaythroughPERC}",{playthroughID})')
	conn.commit()

def editPlaythroughtargetPercent(playthroughID):
	editPlaythroughPercTarg = input("What is the percent playthrough Target(0-100)?: ")
	while editPlaythroughPercTarg > 100 and editPlaythroughPercTarg < 0:
		print("Error the value was not in range 0-100, please enter another Description")
		editPlaythroughPERCTarg = input("What is the percent in the playthrough(must be 0-100)?: ")
	cursor.execute(f'call changePTPERCTarg("{editPlaythroughPERCTarg}",{playthroughID})')
	conn.commit()

def editPlaythroughEndDate(playthroughID):

	#insert the update edit playthroughEnddate to be the curDate()
