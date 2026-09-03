# Create an empty shopping list
shopping_list = []

# Ask the user how many items they want to buy
number_of_items = int(input("How many grocery items do you need? "))

# Repeat the following code that many times
for i in range(number_of_items):

    # Ask for a grocery item
    item = input("Enter grocery item: ")

    # Add that item to our list
    shopping_list.append(item)

# Print a heading
print("\nYour Shopping List:")

# Loop through every item in the shopping list
for item in shopping_list:

    # Display each item
    print("-", item)

# Display how many items are on the list
print("Total items:", len(shopping_list))
