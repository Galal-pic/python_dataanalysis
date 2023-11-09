# Get a list of students' grades from the user
grades_str = input("Enter the list of students' grades separated by spaces: ")

# Split the input string into a list of grades
grades = [int(grade) for grade in grades_str.split()]

# Initialize the count of invalid grades
invalid_count = 0

# Check each grade for validity
for grade in grades:
    if 0 <= grade <= 100:
        print(f"Grade {grade}: Valid")
    else:
        print(f"Grade {grade}: Invalid")
        invalid_count += 1

# Display the count of invalid grades
print(f"Number of invalid grades: {invalid_count}")
