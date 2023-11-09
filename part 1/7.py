# Get the user's full name
full_name = input("Enter name: ")

# Split the full name into words
name_parts = full_name.split()

# Get the first name and last name
first_name = name_parts[0]
last_name = name_parts[-1]

# Display the result
print(f"Your first name is: {first_name}")
print(f"Your last name is: {last_name}")
