import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to gametracker MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', database='gametrackerdb', user='root', password='csi3450gametracker')
        if conn.is_connected():
            print('Connected to MySQL database.')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            return conn

if __name__ == '__main__':
    connect()
