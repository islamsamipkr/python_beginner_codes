# Ask the customer's age
age = int(input("Enter your age: "))

# Children under 5 enter free
if age < 5:
    price = 0

# Children from 5 to 12 pay $8
elif age <= 12:
    price = 8

# Seniors aged 65 or older pay $10
elif age >= 65:
    price = 10

# Everyone else pays the regular price
else:
    price = 15

# Display the ticket price
print("Your movie ticket costs: $", price)

# Give a special message if the movie is free
if price == 0:
    print("Free movie! 🍿")
