import pandas as pd
from mysql.connector import Error


def insert_users_partitions(conn):
    cursor = conn.cursor()
    try:
        selectAllUsers = "SELECT * FROM Users;"

        cursor.execute(selectAllUsers)
        usersData = cursor.fetchall()

        insertBasicQuery = ("INSERT INTO UsersBasic (UserID, UserName, FirstName, LastName, Email)"
                            " VALUES (%s, %s, %s, %s, %s);")

        insertSensitiveQuery = ("INSERT INTO UsersSensitive ("
                                "UserID, Password, PhoneNumber, Address, RegistrationDate, Region, LastLogin)"
                                " VALUES (%s, %s, %s, %s, %s, %s, %s);")

        # Insert data into partitioned tables
        for user in usersData:
            cursor.execute(insertBasicQuery, (user[0], user[1], user[2], user[3], user[4]))
            cursor.execute(insertSensitiveQuery, (user[0], user[5], user[6], user[7], user[8], user[9], user[10]))
            conn.commit()

        print("Data inserted in Users successfully!")

    except Error as e:
        print(f"Error while inserting data in Users: {e}")

    finally:
        cursor.close()
