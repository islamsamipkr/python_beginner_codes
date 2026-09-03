# Create a dictionary containing student names and grades
grades = {
    "Alex": 82,
    "Sara": 95,
    "John": 68,
    "Maria": 88
}

# Start total at zero
total = 0

# Loop through every student and their grade
for student, grade in grades.items():

    # Print their name and grade
    print(student, "scored", grade)

    # Add the grade to the running total
    total = total + grade

# Calculate the average
average = total / len(grades)

# Display the average
print("Class average:", round(average, 2))

# Find the student with the highest grade
top_student = max(grades, key=grades.get)

# Display the top student
print("Top student:", top_student)

# Display their grade
print("Top grade:", grades[top_student])
