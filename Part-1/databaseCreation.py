from mysql.connector import Error

def create_database(conn, dbname):
    cursor = conn.cursor()
    createDBQuery = "CREATE DATABASE IF NOT EXISTS " + dbname
    showDatabasesQuery = "SHOW DATABASES"
    useDBQuery = "USE " + dbname + ";"

    try:
        cursor.execute(createDBQuery)
        conn.commit()
    except Error as e:
        print(f"Error creating database: {e}")

    try:
        cursor.execute(showDatabasesQuery)
        results = cursor.fetchall()
        for row in results:
            print(row)
        print("Query executed successfully")
    except Error as e:
        print(f"Error fetching databases: {e}")

    try:
        cursor.execute(useDBQuery)
    except Error as e:
        print(f"Unable to use database: {e}")
    cursor.close()


def create_table(conn, tableQuery):
    cursor = conn.cursor()

    try:
        cursor.execute(tableQuery)
        conn.commit()
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error creating table {tableQuery}: {e}")

    finally:
        cursor.close()