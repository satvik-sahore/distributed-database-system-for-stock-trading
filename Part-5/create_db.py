from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['pvs_stock_trading']
users_collection = db['Users']
accounts_collection = db['Accounts']
portfolio_data_collection = db['PortfolioData']
orders_collection = db['Orders']
market_data_collection = db['MarketData']
stock_price_history_collection = db['StockPriceHistory']
users_collection.create_index("Email", unique=True)
accounts_collection.create_index("UserID")
portfolio_data_collection.create_index("PortfolioID")
orders_collection.create_index([("AccountID", 1), ("OrderType", 1)])
market_data_collection.create_index("StockSymbol", unique=True)
stock_price_history_collection.create_index("StockSymbol")

print("Database and collections setup is ready!")