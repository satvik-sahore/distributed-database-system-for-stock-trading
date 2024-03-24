import pandas as pd
from mysql.connector import Error


def insert_users_csv(conn):
    # Read data from CSV file
    userDataFile = "data_files/UsersData.csv"
    data = pd.read_csv(userDataFile)
    cursor = conn.cursor()
    try:
        for i, row in data.iterrows():
            # Assuming the table and columns match the CSV structure
            sql_query = ("INSERT INTO Users (UserID,UserName,FirstName,LastName,Email,Password,PhoneNumber,Address,"
                         "RegistrationDate,Region,LastLogin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
            cursor.execute(sql_query, tuple(row))
            conn.commit()

        print("Data inserted in Users successfully!")

    except Error as e:
        print(f"Error while inserting data in Users: {e}")

    finally:
        cursor.close()


def insert_accounts_csv(conn):
    # Read data from CSV file
    accountsDataFile = "data_files/AccountsData.csv"
    data = pd.read_csv(accountsDataFile)
    cursor = conn.cursor()
    try:
        for i, row in data.iterrows():
            # Assuming the table and columns match the CSV structure
            sql_query = ("INSERT INTO Accounts (AccountID,PortfolioID,UserID,AccountType,Balance,AccountStatus)"
                         "VALUES (%s, %s, %s, %s, %s, %s);")
            cursor.execute(sql_query, tuple(row))
            conn.commit()

        print("Data inserted in Accounts successfully!")

    except Error as e:
        print(f"Error while inserting data in Accounts: {e}")

    finally:
        cursor.close()


def insert_marketdata_csv(conn):
    # Read data from CSV file
    marketDataFile = "data_files/MarketData.csv"
    data = pd.read_csv(marketDataFile)
    cursor = conn.cursor()
    try:
        for i, row in data.iterrows():
            # Assuming the table and columns match the CSV structure
            sql_query = ("INSERT INTO MarketData (StockSymbol, StockName, CurrentPrice, OpeningPrice, "
                         "PrevClosingPrice, High,Low, Volume, lastUpdated) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s);")
            cursor.execute(sql_query, tuple(row))
            conn.commit()

        print("Data inserted in MarketData successfully!")

    except Error as e:
        print(f"Error while inserting data in MarketData: {e}")

    finally:
        cursor.close()


def insert_stock_price_history_csv(conn):
    # Read data from CSV file
    stockPriceHistoryFile = "data_files/Merged_Historical_Stock_Data.csv"
    data = pd.read_csv(stockPriceHistoryFile)
    cursor = conn.cursor()
    try:
        for i, row in data.iterrows():
            # Assuming the table and columns match the CSV structure
            sql_query = ("INSERT INTO StockPriceHistory (StockSymbol, Price, RecordedDateTime)"
                         "VALUES (%s, %s, %s);")
            cursor.execute(sql_query, tuple(row))
            conn.commit()

        print("Data inserted in StockPriceHistory successfully!")

    except Error as e:
        print(f"Error while inserting data in StockPriceHistory: {e}")

    finally:
        cursor.close()


def insert_orders_data_csv(conn):
    # Read data from CSV file
    ordersDataFile = "data_files/Orders_Data.csv"
    data = pd.read_csv(ordersDataFile)
    cursor = conn.cursor()
    try:
        for i, row in data.iterrows():
            # Assuming the table and columns match the CSV structure
            sql_query = ("INSERT INTO Orders (OrderId, AccountID, StockSymbol, OrderType, Quantity, OrderPrice, "
                         "Amount, OrderStatus, OrderDate)"
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);")
            cursor.execute(sql_query, tuple(row))
            conn.commit()

        print("Data inserted in Orders successfully!")

    except Error as e:
        print(f"Error while inserting data in Orders: {e}")

    finally:
        cursor.close()


def insert_portfolio_data(conn):
    # Read data from CSV file
    cursor = conn.cursor(buffered=True)
    try:
        ordersQuery = "SELECT * FROM Orders;"
        cursor.execute(ordersQuery)
        records = cursor.fetchall()
        for record in records:
            acId = record[1]
            portfolioIDQuery = "SELECT portfolioID from Accounts WHERE accountID = %s;"
            cursor.execute(portfolioIDQuery, [acId])
            results = cursor.fetchall()
            pfID = results[0][0]

            upsertPortfolioDataQuery = ("INSERT INTO PortfolioData (PortfolioID, StockSymbol, Quantity, TotalAmount) "
                                        "VALUES (%s, %s, %s, %s) "
                                        "ON DUPLICATE KEY UPDATE "
                                        "Quantity = IF(%s = 'buy', Quantity + VALUES(Quantity), Quantity - VALUES(Quantity)), "
                                        "TotalAmount = IF(%s = 'buy', TotalAmount + VALUES(TotalAmount), TotalAmount - VALUES(TotalAmount));")

            cursor.execute(upsertPortfolioDataQuery, [pfID, record[2], record[4], record[6], record[3], record[3]])

            conn.commit()
        print("PortfolioData Inserted successfully!")

    except Error as e:
        print(f"Error while inserting data in PortfolioData: {e}")

    finally:
        cursor.close()