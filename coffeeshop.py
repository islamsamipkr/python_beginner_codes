# Ask the customer how many coffees they want
coffee_count = int(input("How many coffees would you like? "))

# Store the price of one coffee
coffee_price = 3.50

# Calculate the total price
total = coffee_count * coffee_price

# Display the final amount
print("Your total bill is: $", total)

# Check if the customer bought 3 or more coffees
if coffee_count >= 3:
    # Give them a friendly message
    print("You are officially a coffee lover! ☕")
else:
    # This runs when they bought fewer than 3
    print("Enjoy your coffee!")
