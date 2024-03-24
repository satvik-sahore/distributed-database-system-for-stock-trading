import connection
import databaseCreation as dc
import initialDataInsertion as di
import dataRetrieval as dr

# Database details
HOST = ""
PORT = 3307
USERNAME = "root"
PASSWORD = "root"
DATABASE = "pvs_stock_trading"

USERS_TABLE = "Users"
ACCOUNTS_TABLE = "Accounts"
PORTFOLIO_TABLE = "PortfolioData"
ORDERS_TABLE = "Orders"
MARKET_DATA_TABLE = "MarketData"
STOCK_PRICE_HISTORICAL_DATA_TABLE = "StockPriceHistory"
REPLICATION_MANAGEMENT_TABLE = "ReplicationManagement"

# Connecting to database and creating the database:
conn = connection.create_connection(USERNAME, PASSWORD, HOST, PORT)
dc.create_database(conn, DATABASE)

# All tables queries and function calls to create tables:
USERS_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS Users ("
                     "UserID INT AUTO_INCREMENT PRIMARY KEY,"
                     "UserName VARCHAR(255) NOT NULL,"
                     "FirstName VARCHAR(255) NOT NULL,"
                     "LastName VARCHAR(255) NOT NULL,"
                     "Email VARCHAR(255) NOT NULL UNIQUE,"
                     "Password VARCHAR(255) NOT NULL,"
                     "PhoneNumber VARCHAR(15),"
                     "Address TEXT,"
                     "RegistrationDate TIMESTAMP,"
                     "Region VARCHAR(255) NOT NULL,"
                     "LastLogin TIMESTAMP);")
dc.create_table(conn, USERS_TABLE_QUERY)

ACCOUNTS_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS Accounts ("
                        "AccountID INT AUTO_INCREMENT PRIMARY KEY,"
                        "PortfolioID INT,"
                        "UserID INT NOT NULL,"
                        "AccountType VARCHAR(50),"
                        "Balance FLOAT(10, 2),"
                        "AccountStatus VARCHAR(50),"
                        "UNIQUE (PortfolioID),"
                        "FOREIGN KEY (UserID) REFERENCES Users(UserID));")
dc.create_table(conn, ACCOUNTS_TABLE_QUERY)

PORTFOLIO_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS PortfolioData ("
                         "PortfolioID INT NOT NULL,"
                         "StockSymbol VARCHAR(10) NOT NULL,"
                         "Quantity INT NOT NULL,"
                         "TotalAmount FLOAT(10, 2) NOT NULL,"
                         "FOREIGN KEY (PortfolioID) REFERENCES Accounts(PortfolioID),"
                         "PRIMARY KEY (PortfolioID, StockSymbol));")
dc.create_table(conn, PORTFOLIO_TABLE_QUERY)

ORDERS_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS Orders ("
                      "OrderID INT AUTO_INCREMENT,"
                      "AccountID INT NOT NULL,"
                      "StockSymbol VARCHAR(10) NOT NULL,"
                      "OrderType VARCHAR(10) NOT NULL,"
                      "Quantity INT NOT NULL,"
                      "OrderPrice FLOAT(10, 2) NOT NULL,"
                      "Amount FLOAT(10, 2),"
                      "OrderStatus VARCHAR(50) NOT NULL,"
                      "OrderDate TIMESTAMP NOT NULL,"
                      "PRIMARY KEY (OrderID, AccountID, OrderType));")
dc.create_table(conn, ORDERS_TABLE_QUERY)

MARKET_DATA_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS MarketData ("
                           "StockSymbol VARCHAR(10) PRIMARY KEY,"
                           "StockName VARCHAR(255),"
                           "CurrentPrice FLOAT(10, 2),"
                           "OpeningPrice FLOAT(10, 2),"
                           "PrevClosingPrice FLOAT(10, 2),"
                           "High FLOAT(10, 2),"
                           "Low FLOAT(10, 2),"
                           "Volume BIGINT,"
                           "LastUpdated TIMESTAMP);")
dc.create_table(conn, MARKET_DATA_TABLE_QUERY)

STOCK_PRICE_HISTORICAL_DATA_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS StockPriceHistory ("
                                           "HistoryID INT AUTO_INCREMENT,"
                                           "StockSymbol VARCHAR(10),"
                                           "Price FLOAT(10, 2),"
                                           "RecordedDateTime TIMESTAMP,"
                                           "PRIMARY KEY (HistoryId, StockSymbol));")
dc.create_table(conn, STOCK_PRICE_HISTORICAL_DATA_TABLE_QUERY)

REPLICATION_MANAGEMENT_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS ReplicationManagement ("
                                      "ReplicationID INT AUTO_INCREMENT PRIMARY KEY,"
                                      "TableName VARCHAR(255),"
                                      "ReplicationStatus VARCHAR(50),"
                                      "LastReplicated TIMESTAMP,"
                                      "ReplicationNode VARCHAR(255),"
                                      "ChangeLog TEXT);")
dc.create_table(conn, REPLICATION_MANAGEMENT_TABLE_QUERY)

# Function calls to insert data in the tables:
di.insert_users_csv(conn)

di.insert_accounts_csv(conn)

di.insert_marketdata_csv(conn)

#di.insert_stock_price_history_csv(conn)

di.insert_orders_data_csv(conn)

di.insert_portfolio_data(conn)

# Function calls for data retrival:
dr.select_all(conn, USERS_TABLE)
dr.select_all(conn, ACCOUNTS_TABLE)
dr.select_all(conn,PORTFOLIO_TABLE)
dr.select_all(conn, ORDERS_TABLE)
dr.select_all(conn, MARKET_DATA_TABLE)
dr.select_all(conn, STOCK_PRICE_HISTORICAL_DATA_TABLE)

dr.select_specific_account(conn, 1)

dr.select_user_portfolio(conn, 5)

dr.select_buy_orders(conn, "TCS", "buy", 10000)

dr.select_market_data(conn, "GOOGL")

dr.select_stock_prices_history(conn, "AAPL", "2023-11-13 9:00:00", "2023-11-13 9:01:00")