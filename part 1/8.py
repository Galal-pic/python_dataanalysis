# Get a statement from the user
statement = input("Enter a statement: ")

# Convert the statement to lowercase to make it case-insensitive
statement = statement.lower()

# Initialize a variable to count vowels
vowel_count = 0

# Define the set of vowels
vowels = set("aeiou")

# Count the number of vowels in the statement
for char in statement:
    if char in vowels:
        vowel_count += 1

# Display the result
if vowel_count > 0:
    print(f"The number of vowels in the statement is: {vowel_count}")
else:
    print("No vowels found.")
