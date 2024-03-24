from mysql.connector import Error


def vertical_partition_data(conn, table):
    cursor = conn.cursor()

    try:
        selectQuery = f"SELECT * FROM {table} LIMIT 10;"  # Limiting search result to 10 for display purposes.
        cursor.execute(selectQuery)
        records = cursor.fetchall()
        print(f"{table} table data:")
        for record in records:
            print(record)
        print()

    except Error as e:
        print(f"Error retrieving data from partitioned table {table} table: {e}")

    finally:
        cursor.close()


def horizontal_partition_data(conn, table, partition):
    cursor = conn.cursor()

    try:
        selectQuery = f"SELECT * FROM {table} PARTITION ({partition}) LIMIT 10;"  # Limiting search result to 10 for display purposes.
        cursor.execute(selectQuery)
        records = cursor.fetchall()
        print(f"{table} table data:")
        for record in records:
            print(record)
        print()

    except Error as e:
        print(f"Error retrieving data from horiontal partitioned {table} table: {e}")

    finally:
        cursor.close()

