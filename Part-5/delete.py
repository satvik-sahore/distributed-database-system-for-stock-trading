from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['pvs_stock_trading']

db.Users.delete_one(
    {"UserName": "user1"}
)

db.Accounts.delete_many(
    {"Balance": {"$lt": 100.0}}
)

db.Orders.delete_one(
    {"OrderID": "<your_order_id>"}
)

db.PortfolioData.delete_many(
    {"StockSymbol": "AAPL"}
)

from datetime import datetime, timedelta
cutoff_date = datetime.now() - timedelta(days=30)
db.MarketData.delete_many(
    {"LastUpdated": {"$lt": cutoff_date}}
)

print("Documents deleted successfully!")