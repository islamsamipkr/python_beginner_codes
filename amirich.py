# Ask for the user's hourly salary
hourly_rate = float(input("How much do you make per hour? $"))

# Ask how many hours they work every week
hours_per_week = float(input("How many hours do you work per week? "))

# Assume there are 52 weeks in one year
weeks_per_year = 52

# Calculate yearly income
yearly_income = hourly_rate * hours_per_week * weeks_per_year

# Show the estimated yearly salary
print("Estimated yearly salary: $", round(yearly_income, 2))

# Check the salary range
if yearly_income >= 100000:
    # Runs if salary is $100,000 or more
    print("Six-figure club! 💰")

elif yearly_income >= 60000:
    # Runs if salary is between $60,000 and $99,999
    print("You're doing pretty well!")

else:
    # Runs if salary is below $60,000
    print("Keep building those skills! 🚀")
