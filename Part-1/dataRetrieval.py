from mysql.connector import Error


def select_all(conn, table):
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
        print(f"Error retrieving data from {table} table: {e}")

    finally:
        cursor.close()


def select_specific_account(conn, accountId):
    cursor = conn.cursor()
    try:
        selectPortfolioQuery = "SELECT * FROM Accounts where AccountID = %s;"
        cursor.execute(selectPortfolioQuery, [accountId])

        print(f"Account details for the account with id - {accountId}:")
        records = cursor.fetchall()
        for record in records:
            print(record)
        print()

    except Error as e:
        print(f"Error retrieving data for the specified account: {e}")

    finally:
        cursor.close()


def select_user_portfolio(conn, userId):
    cursor = conn.cursor()
    try:
        selectUserPortfolioQuery = ("SELECT * FROM PortfolioData WHERE PortfolioID = (SELECT PortfolioID FROM Accounts "
                                    "WHERE UserId = %s);")
        cursor.execute(selectUserPortfolioQuery, [userId])

        print(f"Portfolio details for the with id - {userId}:")
        records = cursor.fetchall()
        for record in records:
            print(record)
        print()

    except Error as e:
        print(f"Error retrieving portfolio data for the user - {userId}: {e}")

    finally:
        cursor.close()


def select_buy_orders(conn, stock, orderType, amount):
    cursor = conn.cursor()
    try:
        selectOrdersQuery = "SELECT * FROM Orders WHERE StockSymbol = %s and OrderType = %s and Amount >= %s LIMIT 10;"
        cursor.execute(selectOrdersQuery, [stock, orderType, amount])

        print(f"{orderType} order details for {stock} stock with amount greater than {amount}:")
        records = cursor.fetchall()
        for record in records:
            print(record)
        print()

    except Error as e:
        print(f"Error retrieving order details for the stock {stock}: {e}")

    finally:
        cursor.close()


def select_market_data(conn, stock):
    cursor = conn.cursor()
    try:
        selectMarketData = "SELECT * FROM MarketData WHERE StockSymbol = %s;"
        cursor.execute(selectMarketData, [stock])

        print(f"Current details for the stock {stock}:")
        records = cursor.fetchall()
        for record in records:
            print(record)
        print()

    except Error as e:
        print(f"Error retrieving the latest stock details for {stock}: {e}")

    finally:
        cursor.close()


def select_stock_prices_history(conn, stock, start, end):
    cursor = conn.cursor()
    try:
        selectStockHistoryQuery = "SELECT * FROM StockPriceHistory WHERE StockSymbol = %s AND RecordedDateTime BETWEEN %s AND %s LIMIT 10;"
        cursor.execute(selectStockHistoryQuery, [stock, start, end])

        print(f"Stock price history for {stock} between {start} and {end}")
        records = cursor.fetchall()
        for record in records:
            print(record)
        print()

    except Error as e:
        print(f"Error fetch stock price history for {stock}: {e}")

    finally:
        cursor.close()
