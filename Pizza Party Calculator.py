# Import math so we can use math.ceil()
import math

# Ask how many people are coming
people = int(input("How many people are coming to the party? "))

# Assume every person eats 3 pizza slices
slices_per_person = 3

# Assume one pizza has 8 slices
slices_per_pizza = 8

# Calculate the total number of slices needed
total_slices = people * slices_per_person

# Calculate pizzas needed
# math.ceil rounds UP because we cannot order 0.5 of a pizza
pizzas_needed = math.ceil(total_slices / slices_per_pizza)

# Display the result
print("You need", total_slices, "pizza slices.")

# Display how many pizzas should be ordered
print("You should order", pizzas_needed, "pizzas.")
