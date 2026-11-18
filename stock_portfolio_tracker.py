
# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

total_investment = 0

# Taking number of stocks from user
n = int(input("Enter number of stocks: "))

# Taking stock details
for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        print("Stock:", stock_name)
        print("Price:", price)
        print("Quantity:", quantity)
        print("Investment:", investment)

    else:
        print("Stock not available!")

# Display total investment
print("\nTotal Investment Value:", total_investment)

# Saving result in a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Report\n")
    file.write("----------------------\n")
    file.write("Total Investment: " + str(total_investment))

print("\nResult saved successfully!")
