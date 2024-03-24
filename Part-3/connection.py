import mysql.connector
from mysql.connector import Error

def create_connection(user_name, user_password, host_name="", port=3306, db_name=None):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port=port,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection