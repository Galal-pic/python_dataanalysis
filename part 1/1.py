# Get a number N from the user
N = int(input("Enter a number N: "))

# Check if the number is negative
if N < 0:
    print("The number is negative.")
else:
    # Calculate the summation of numbers from 1 to N
    summation = sum(range(1, N + 1))
    print(f"The summation of numbers from 1 to {N} is: {summation}")
