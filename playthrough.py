
#Gregory Sylveser
#3/30/2024
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


#temp values for the scope of the playthrough script

#change UserID when logining in 
userID = null

#change gameID python script needed to choose which game
gameID = null


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




#not sure if we need this
#toDo:debug, output table for user to view when chooseing
#function: edits run playthoughID with appropriate values
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



#still need to insert
def editPlaythroughName(playthroughID):
	editPlaythroughName = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")
	while len(editPlaythrougnName) >= 45:
		print("error the length of the string input is too long, please enter another name")
		editPlaythroughName = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")
	
	#insert update cursor statement 

def editPlaythroughDes(playthroughID):
	editPlaythroughDesc = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")


	#insert update cursor statement 
	
def editPlaythroughPercent(playthroughID):
	editPlaythroughPercent = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")

	#insert update cursor statement 

def editPlaythroughtargetPercent(playthroughID):
	editPlaythroughTargetPercent = input("What would you like to change the name of the playthrough to(must be less than 45 characters)?: ")

	#insert update cursor statement 

def editPlaythroughEndDate(playthroughID):
	#change the end date tot be a flag that will take the current date
	editPlaythroughEndDatetarget
	#insert update cursor statement 
