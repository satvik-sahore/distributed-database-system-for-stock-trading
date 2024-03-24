"""read latest data from market data
randomly increse or decrease prices
insert data in stock price history"""
import connection
from mysql.connector import Error
import random
import time

# Database details
HOST = ""
PORT = 3307
USERNAME = "root"
PASSWORD = "root"
DATABASE = "pvs_stock_trading"

# Connecting to database and creating the database:
conn = connection.create_connection(USERNAME, PASSWORD, HOST, PORT, DATABASE)


def stimulate_stock_market(conn):
    cursor = conn.cursor()

    try:
        selectQuery = f"SELECT * FROM MarketData;"  # Limiting search result to 10 for display purposes.
        cursor.execute(selectQuery)

        records = cursor.fetchall()
        print("MarketData table data:")
        for record in records:
            print(record)
        print()

        aapl = records[0][2]
        googl = records[1][2]
        msft = records[2][2]
        tcs = records[3][2]
        percentage_range = (0.2, 3)
        while(True):
            percentage_change = random.uniform(*percentage_range)

            # Randomly decide to increase or decrease
            if random.choice([True, False]):
                # Increase the value
                aapl = aapl * (1 + percentage_change / 100)
                googl = googl * (1 + percentage_change / 100)
                msft = msft * (1 + percentage_change / 100)
                tcs = tcs * (1 + percentage_change / 100)
            else:
                # Decrease the value
                aapl = aapl * (1 - percentage_change / 100)
                googl = googl * (1 - percentage_change / 100)
                msft = msft * (1 - percentage_change / 100)
                tcs = tcs * (1 - percentage_change / 100)

            try:
                conn.start_transaction()
                insertStockPrice = ("INSERT INTO StockPriceHistory (StockSymbol,Price,RecordedDateTime) "
                                    "VALUES"
                                    "('AAPL', %s, NOW()),"
                                    "('GOOGL',%s, NOW()),"
                                    "('MSFT', %s, NOW()),"
                                    "('TCS', %s, NOW());")

                cursor.execute(insertStockPrice, [aapl, googl, msft, tcs])
                conn.commit()
                time.sleep(1)
                print("Stock price updated")

            except Error as e:
                print(f"Transaction failed to update Stock Price, rolling back: {e}")
                conn.rollback()

    except Error as e:
        print(f"Error retrieving data from MaretData table: {e}")

    finally:
        cursor.close()


stimulate_stock_market(conn)
