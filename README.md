# csi3450-game-tracker
### Term project for CSI 3450

### Preface:
The aim of this project is to practice the core ideas that we learned in our intro to SQL databases class. The application use is for storeing information about the users and the playthroughs and games and ratings to store progess of all your games.

### Business rules:
- A user can own many games, but each game can only be owned by a single user. 
- A user can write many ratings, but each rating must be written by only one user.
- A user can manage multiple playthroughs, but each playthrough can only be managed by one user.
- A genre can be applied to multiple games, but each game must only belong to a single genre.
- A game may contain multiple achievements, but each achievement must belong to a single game.
- A game can belong to multiple playthroughs, but each playthrough must involve only one game.
- A game can be given multiple ratings, but each rating must belong to only one game.
- A playthrough can contain multiple achievements, and each achievement can be included in multiple different playthroughs. (results in intersection entity PlaythroughAchievement)

__________
## Index
1. Installation
2. known bugs
3. Afternotes
__________
## 1- Installation

Preface: this installation assumes you are running on a windows 10 operating system with python 3, pip, mysql workbench, and mysql server

To check to see if python 3 is installed as well as the appropriate path variables for the command line follow the steps below:
1. open command prompt, and enter the following commands
 ```cmd
 python --version
 python -m pip --version
 mysql --version
 ```
2. If all of these commands do not return the version then follow the links below for more help
 - https://www.scaler.com/topics/sql/how-to-install-mysql-in-windows-10/
 - https://www.youtube.com/watch?v=lezhrFdVSVY&ab_channel=ExampleProgram
 - https://www.youtube.com/watch?v=a1AMVA9p3W0&t=7s&ab_channel=EngineersRevolution

Below is how you install and run the mysql server:
1. Open up mysqlworkbench and load the dump file into a query execute
 - there is sometimes and issue with the default value of startdate on playthroughs, if this occurs change the default date to '1900-01-01'
2. Connect to database and load and run the following sql scripts in top to bottom order:
 - gametrackerdb-supp.sql (it will say duplicate constraints exist, but this just means they were already added with the dump so ignore it)

Below is how you install and run the mysql server without using the dump file:
1. Open up mysqlworkbench, load and forward engineer the gametrackerdb-model.mwb model
 - there is sometimes and issue with the default value of startdate on playthroughs, if this occurs change the default date to '1900-01-01'
2. Connect to database and load and run the following sql scripts in top to bottom order:
 - gametrackerdb-supp.sql 
 - gametrackerdb-populate.sql (run this if you wish to prepopulate the database)

Below is how you set up and access the server from the command line:
1. open up the file named 'connect.ini' and change the field for user name and password to the ones on your mysql server
2. open up file explore where the files were download, and in the search bar type cmd, which should open the command prompt from the directory
3. enter the following commands
```cmd
python -m pip install -U prettytable
python -m pip install -U mysql.connector
python -m pip install -U mysql.connector.python
```
4. To Run the python script for interaction with the live database run the following command in the directory where main.py is located
```cmd
python main.py
```

___________________
## 2 - known bugs

some commonly known issues at the moment that we will plan on fixxing if we come back to database are as follows:
- use of capitalization, spelling errors, characters such as ' and injection of keywords and mysql code for input
- standardization of layout of options for all choices
- curdate() default value for playthrough.startDate issue when you construct in only some systems, quick fix is to set the default startdate to '1900-01-01'

__________________
## 3 - After notes 

Please feel free to add to this project, if so please update the README to reflect any updates made to the project. 









