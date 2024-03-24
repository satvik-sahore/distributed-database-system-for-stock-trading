import connection
import partitionCreation as pc
import partitionDataInsertion as pdi
import partitionDataRetrieval as pdr

# Database details
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
conn = connection.create_connection(USERNAME, PASSWORD, HOST, PORT, DATABASE)

# Modifying tables to implement Vertical and Horizontal Partitioning:
# Creating two sub-tables of Users table, UsersBasic and UsersSensitive as a part of Vertical Partitioning:
USERS_BASIC_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS UsersBasic ("
                           "UserID INT AUTO_INCREMENT PRIMARY KEY,"
                           "UserName VARCHAR(255) NOT NULL,"
                           "FirstName VARCHAR(255) NOT NULL,"
                           "LastName VARCHAR(255) NOT NULL,"
                           "Email VARCHAR(255) NOT NULL UNIQUE);")
pc.vertical_partitioning(conn, USERS_BASIC_TABLE_QUERY)

USERS_SENSITIVE_TABLE_QUERY = ("CREATE TABLE IF NOT EXISTS UsersSensitive ("
                               "UserID INT PRIMARY KEY,"
                               "Password VARCHAR(255) NOT NULL,"
                               "PhoneNumber VARCHAR(15),"
                               "Address TEXT,"
                               "RegistrationDate TIMESTAMP,"
                               "Region VARCHAR(255) NOT NULL,"
                               "LastLogin TIMESTAMP);")
pc.vertical_partitioning(conn, USERS_SENSITIVE_TABLE_QUERY)

# Altering tables to create partitions in the existing tables
# (MySQL supports creating partitions after creating the tables)

ORDERS_TABLE_PARTITION_QUERY = ("ALTER TABLE Orders "
                                "PARTITION BY LIST COLUMNS(OrderType) ("
                                "PARTITION buy VALUES IN ('buy'),"
                                "PARTITION sell VALUES IN ('sell'));")
pc.horizontal_partitioning(conn, ORDERS_TABLE_PARTITION_QUERY)

STOCK_PRICE_HISTORICAL_DATA_TABLE_PARTITION_QUERY = ("ALTER TABLE StockPriceHistory "
                                                     "PARTITION BY LIST COLUMNS(StockSymbol) ("
                                                     "PARTITION aapl VALUES IN ('AAPL'),"
                                                     "PARTITION googl VALUES IN ('GOOGL'),"
                                                     "PARTITION msft VALUES IN ('MSFT'),"
                                                     "PARTITION tcs VALUES IN ('TCS'));")
pc.horizontal_partitioning(conn, STOCK_PRICE_HISTORICAL_DATA_TABLE_PARTITION_QUERY)

pdi.insert_users_partitions(conn)

# Function calls for data retrival:
pdr.vertical_partition_data(conn, "UsersBasic")

pdr.horizontal_partition_data(conn, "Orders", "sell")

pdr.horizontal_partition_data(conn, "StockPriceHistory", "googl")

