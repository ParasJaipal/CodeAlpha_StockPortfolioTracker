stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

print("Available Stocks:")
for stock in stocks:
    print(stock)

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))

        price = stocks[stock_name]
        investment = price * quantity

        print(f"{stock_name}: ${price} x {quantity} = ${investment}")

        total += investment

    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total)