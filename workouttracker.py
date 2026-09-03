# Create a function called calculate_calories
# It accepts two pieces of information:
# workout_minutes and calories_per_minute
def calculate_calories(workout_minutes, calories_per_minute):

    # Calculate calories burned
    calories = workout_minutes * calories_per_minute

    # Send the answer back
    return calories


# Ask how long the person exercised
minutes = float(input("How many minutes did you exercise? "))

# Ask approximately how many calories are burned each minute
calories_rate = float(input("Calories burned per minute: "))

# Call our function and save its answer
total_calories = calculate_calories(minutes, calories_rate)

# Display the result
print("You burned approximately", round(total_calories), "calories.")

# Give some encouragement
if minutes >= 30:
    print("Great workout! 💪")
else:
    print("A short workout is still better than no workout!")
