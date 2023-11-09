# Get the value of N from the user
N = int(input("Enter the value of N: "))

# Initialize variables for the sum of odd and even elements
sum_odd = 0
sum_even = 0

# Read N numbers from the user
for i in range(N):
    num = int(input(f"Enter number {i + 1}: "))
    
    # Check if the number is odd or even and update the sums accordingly
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# Print the sum of odd and even elements
print(f"Sum of odd elements: {sum_odd}")
print(f"Sum of even elements: {sum_even}")
