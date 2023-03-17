from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def query_with_fetchone():
    
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user LIMIT 10")

    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    query_with_fetchone()
