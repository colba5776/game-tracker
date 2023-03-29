from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()
    #print("Type", type(db_config))
    conn = None
    try:
        # print('Connecting to MySQL database...')
        # Unpack the dictionary arguments 
        conn = MySQLConnection(**db_config)

        """
        if conn.is_connected():
            print('Connection established. \n')
        else:
            print('Connection failed. \n') """

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            #conn.close()
            #print('Connection closed.')
            return conn


if __name__ == '__main__':
    connect()
