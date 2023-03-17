from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from prettytable import from_db_cursor


def query_with_prettytable():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student LIMIT 20")
        x = from_db_cursor (cursor)
        x.align["name"] = "l"
        x.align["dept_name"] = "l"
        x.sortby = "name"
        print(x)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_prettytable()
