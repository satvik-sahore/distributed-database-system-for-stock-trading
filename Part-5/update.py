from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['pvs_stock_trading']  # Replace with your actual database name

# Example updates:
# 1. Update a user's email address
db.Users.update_one(
    {"UserName": "user1"},  # Query: finds the document where UserName is 'user1'
    {"$set": {"Email": "newemail@example.com"}}  # Update: sets the new email address
)

# 2. Update the balance for all accounts of a specific type
db.Accounts.update_many(
    {"AccountType": "Savings"},  # Query: finds all documents with AccountType 'Savings'
    {"$set": {"Balance": 1200.0}}  # Update: sets the new balance for all matching accounts
)

# 3. Update the order status for a specific order
db.Orders.update_one(
    {"OrderID": "<account_id_1>"},  # Replace <your_order_id> with the actual order ID
    {"$set": {"StockSymbol": "GOOG"}}  # Update: sets the new order status
)

# 4. Increment the stock quantity in a portfolio
db.PortfolioData.update_one(
    {"PortfolioID": "<portfolio_id_1>", "StockSymbol": "AAPL"},  # Query criteria
    {"$inc": {"Quantity": 5}}  # Increment the Quantity by 5
)

# 5. Update last updated timestamp in MarketData for a specific stock
from datetime import datetime
db.MarketData.update_one(
    {"StockSymbol": "AAPL"},
    {"$set": {"LastUpdated": datetime.now()}}
)

print("Documents updated successfully!")