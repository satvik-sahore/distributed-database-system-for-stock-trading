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


def buy_stock(conn, accountId, stockSymbol, quantity):
    cursor = conn.cursor()
    try:
        conn.start_transaction()
        selectQuery = f"SELECT CurrentPrice from MarketData where StockSymbol = '{stockSymbol}';"
        cursor.execute(selectQuery)
        results = cursor.fetchall()

        orderPrice = results[0][0]
        amount = quantity * orderPrice
        orderId = 11211

        createSellOrder = ("INSERT INTO Orders (OrderId, AccountID,StockSymbol,OrderType,Quantity,OrderPrice,Amount,"
                          "OrderStatus,OrderDate)"
                          "VALUES (%s, %s, %s, 'sell', %s, %s, %s, 'placed', NOW());")
        cursor.execute(createSellOrder, [orderId, accountId, stockSymbol, quantity, orderPrice, amount])
        conn.commit()

        conn.start_transaction()
        checkBuyOrderQuery = ("SELECT * FROM Orders where OrderType = 'buy' and OrderStatus = "
                               "'placed' and StockSymbol = %s and Quantity = %s order by OrderId;")
        cursor.execute(checkBuyOrderQuery, [stockSymbol, quantity])
        res = cursor.fetchall()
        for r in res:
            print(res)
            print(res[0][1], res[0][4])
        buyAccountId = res[0][1]
        buyOrderId = res[0][0]
        if res:
            updateBuyPortfolioQuery = ("UPDATE PortfolioData SET Quantity = Quantity + %s WHERE PortfolioID = (SELECT "
                                        "PortfolioID from Accounts WHERE AccountID = %s) and StockSymbol = %s;")
            cursor.execute(updateBuyPortfolioQuery, [quantity, buyAccountId, stockSymbol])

            updateBuyOrder = "UPDATE Orders SET OrderStatus = 'fulfilled' WHERE OrderId = %s;"
            cursor.execute(updateBuyOrder, [buyOrderId])

            updateSellPortfolioQuery = ("UPDATE PortfolioData SET Quantity = Quantity - %s WHERE PortfolioID = (SELECT "
                                       "PortfolioID from Accounts WHERE AccountID = %s) and StockSymbol = %s;")
            cursor.execute(updateSellPortfolioQuery, [quantity, accountId, stockSymbol])

            updateSellOrder = "UPDATE Orders SET OrderStatus = 'fulfilled' WHERE OrderId = %s;"
            cursor.execute(updateSellOrder, [orderId])

            conn.commit()

    except Error as e:
        print(f"Error creating order: {e}")


buy_stock(conn, 1, 'AAPL', 10)
