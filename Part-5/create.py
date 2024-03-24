import json
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['pvs_stock_trading']

def read_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

users_file = 'data/UsersData.json'
accounts_file = 'data/Accounts.json'
portfolio_data_file = 'data/PortfolioData.json'
orders_file = 'data/Orders.json'
market_data_file = 'data/MarketData.json'
stock_price_history_file = 'data/StockPriceHistory.json'

users_data = read_data_from_json(users_file)
accounts_data = read_data_from_json(accounts_file)
portfolio_data = read_data_from_json(portfolio_data_file)
orders_data = read_data_from_json(orders_file)
market_data = read_data_from_json(market_data_file)
stock_price_history = read_data_from_json(stock_price_history_file)

db.Users.insert_many(users_data)
db.Accounts.insert_many(accounts_data)
db.PortfolioData.insert_many(portfolio_data)
db.Orders.insert_many(orders_data)
db.MarketData.insert_many(market_data)
db.StockPriceHistory.insert_many(stock_price_history)

print("Data inserted successfully!")