stocks = {
    "NFLX": 435,
    "AMZN": 135,
    "META": 300,
    "IBM": 160,
    "ORCL": 133
}
total_value = 0
print("----- Stock Tracker -----")
print("\nAvailable Stocks:")
for stock, price in stocks.items():
    print(stock, ":", price)
while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stocks:
        qty = int(input("Enter quantity: "))
        value = stocks[stock] * qty
        total_value += value
        print("Stock Price:", stocks[stock])
        print("Investment Value:", value)
    else:
        print("Stock not available.")
print("\nTotal Investment =", total_value)
# Save data to a CSV file
with open("stock_data.csv", "w") as file:
    file.write("Total Investment," + str(total_value))
print("Investment details saved in stock_data.csv")
