# Read the number N from the user
N = int(input("Enter a number N: "))

# Print the multiplication table
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(i * j, end='\t')
    print()
