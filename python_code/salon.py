
# List of different hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Prices corresponding to each hairstyle 
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Number of haircuts performed for each hairstyle last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Initialize a variable to track the total price of all haircuts
total_price = 0

# Calculate the total price by summing up individual prices 
for price in prices:
  total_price += price

# Calculate the average haircut price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# Create a new list of prices after applying a discount of 5 dollars 
new_prices = [price - 5 for price in prices]
print(new_prices)

# Initialize a variable to keep track of total revenue 
total_revenue = 0 

# Calculate the total revenue by multiplying prices with the number of haircuts 
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# Calculate the average daily revenue 
average_daily_revenue = total_revenue / 7
print("Total Revenue:" + str(total_revenue))
print("Average Daily Revenue:", average_daily_revenue)

# Create a list of hairstyles that have a price under 30 dollars 
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) -1) if new_prices[i]< 30]
print("Haircuts under 30 dollars:", cuts_under_30)

  

