import mysql.connector
from prettytable import from_db_cursor
from connect_dbconfig import connect

#conneciton to the database
conn = connect()
cursor = conn.cursor()
cursor.execute("USE gametrackerdb;")

def manage_playthroughs(userId):
	# List out all the playthroughs in the database
    list_playthroughs(None)
    # While the user still wants to do something here
    done = False
    while (not done):
        # Ask whether the user would like to view playthroughs, or edit them
        userInput = None
        while (userInput != 'S' and userInput != 'E' and userInput != 'V' and userInput != 'B'):
            userInput = input("Enter [S] to Search, [V] to View, [E] to Edit or Add, [B] to go Back: ")

        # If they wish to search for a playthrough
        if (userInput == 'S'):
            search_playthroughs()
        # If they wish to view info on a playthrough
        if (userInput == 'V'):
            view_playthrough(userId)
        # If they wish to edit a playthrough
        if (userInput == 'E'):
            edit_playthrough(userId)
        # If they wish to leave
        if (userInput == 'B'):
            done = True

def search_playthroughs():
	# Implement here
	print("Placeholder")
def view_playthrough():
	# Implement here
	print("Placeholder")
def edit_playthrough():
	# Implement here
	print("Placeholder")

""" Used to list out all the playthroughs """
""" If userId is specified then only list playthroughs for that user """
def list_playthroughs(userId):
    # Execute the query to get the playthroughs list
    cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}';")
    # Check if we only want to list playthroughs for a specific user
    if (userId is not None):
        cursor.execute(f"SELECT * FROM playthrough WHERE userId='{userId}';")
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