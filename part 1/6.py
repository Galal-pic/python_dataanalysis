# Get one-digit numbers from the user
units = int(input("Please enter units: "))
tens = int(input("Please enter tens: "))
hundreds = int(input("Please enter hundreds: "))

# Form the 3-digit number
result_number = hundreds * 100 + tens * 10 + units

# Display the result
print(f"The number is: {result_number}")
