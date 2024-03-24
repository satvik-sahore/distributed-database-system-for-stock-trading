from mysql.connector import Error


def vertical_partitioning(conn, tableQuery):
    cursor = conn.cursor()

    try:
        cursor.execute(tableQuery)
        conn.commit()
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error creating table: {e}")

    finally:
        cursor.close()


def horizontal_partitioning(conn, tableQuery):
    cursor = conn.cursor()

    try:
        cursor.execute(tableQuery)
        conn.commit()
        results = cursor.fetchall()
        for row in results:
            print(row)

    except Error as e:
        print(f"Error creating horizontal partitions: {e}")

    finally:
        cursor.close()
