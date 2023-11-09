# Get the total number of glasses (X) from the user
X = int(input("Enter the total number of glasses: "))

# Get the number of glasses per tray (Y) from the user
Y = int(input("Enter the number of glasses per tray: "))

# Calculate the number of trays needed
N = (X + Y - 1) // Y

# Display the result
print(f"The number of trays needed is: {N}")
