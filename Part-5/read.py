from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['pvs_stock_trading']

users_data = db.Users.find()
accounts_data = db.Accounts.find()
portfolio_data = db.PortfolioData.find()
orders_data = db.Orders.find()
market_data = db.MarketData.find()
stock_price_history_data = db.StockPriceHistory.find()

def print_documents(collection_name, documents):
    print(f"\nDocuments in {collection_name} collection:")
    for doc in documents:
        print(doc)

print_documents("Users", users_data)
print_documents("Accounts", accounts_data)
print_documents("PortfolioData", portfolio_data)
print_documents("Orders", orders_data)
print_documents("MarketData", market_data)
print_documents("StockPriceHistory", stock_price_history_data)