Table Users {
  UserID int [pk, increment] // Auto increment primary key
  UserName varchar(255) [not null]
  FirstName varchar(255) [not null]
  LastName varchar(255) [not null]
  Email varchar(255) [not null, unique]
  Password varchar(255) [not null]
  PhoneNumber varchar(15)
  Address text
  RegistrationDate datetime
  Region varchar(255) [not null]
  LastLogin datetime
}

Table Accounts {
  AccountID int [pk, increment] // Auto increment primary key
  PortfolioID int [unique]
  UserID int [not null]
  AccountType varchar(50)
  Balance decimal(10, 2)
  AccountStatus varchar(50)
  Foreign Key (UserID)
  References Users(UserID)
}

Table PortfolioData {
  PortfolioID int [not null]
  StockSymbol varchar(10) [not null]
  Quantity int [not null]
  TotalAmount decimal(10, 2) [not null]
  Foreign Key (PortfolioID)
  References Accounts(PortfolioID)
  Primary Key (PortfolioID, StockSymbol)
}

Table Orders {
  OrderID int [pk, increment] // Auto increment primary key
  AccountID int [not null]
  StockSymbol varchar(10) [not null]
  OrderType varchar(10) [not null]
  Quantity int [not null]
  OrderPrice decimal(10, 2) [not null]
  Amount decimal(10, 2)
  OrderStatus varchar(50) [not null]
  OrderDate datetime [not null]
  Foreign Key (AccountID)
  References Accounts(AccountID)
}

Table MarketData {
  StockSymbol varchar(10) [pk] // Primary key
  StockName varchar(255)
  CurrentPrice decimal(10, 2)
  OpeningPrice decimal(10, 2)
  PrevClosingPrice decimal(10, 2)
  High decimal(10, 2)
  Low decimal(10, 2)
  Volume bigint
  LastUpdated datetime
}

Table StockPriceHistory {
  HistoryID int [pk, increment] // Auto increment primary key
  StockSymbol varchar(10)
  Price decimal(10, 2)
  RecordedDateTime datetime
  Foreign Key (StockSymbol)
  References MarketData(StockSymbol)
}

Table ReplicationManagement {
  ReplicationID int [pk, increment] // Auto increment primary key
  TableName varchar(255)
  ReplicationStatus varchar(50)
  LastReplicated datetime
  ReplicationNode varchar(255)
  ChangeLog text
}

// Relationships
Ref: Accounts.UserID > Users.UserID // Accounts to Users (many-to-one)
Ref: PortfolioData.PortfolioID > Accounts.PortfolioID // PortfolioData to Accounts (many-to-one)
Ref: Orders.AccountID > Accounts.AccountID // Orders to Accounts (many-to-one)
Ref: StockPriceHistory.StockSymbol > MarketData.StockSymbol // StockPriceHistory to MarketData (many-to-one)

