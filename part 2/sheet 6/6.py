def calculate_area(length, width):
    return round(length * width)

num_rectangles = int(input("Enter the number of rectangles: "))

lengths = []
widths = []

for i in range(1, num_rectangles + 1):
    length = float(input(f"Enter the length of rectangle {i}: "))
    width = float(input(f"Enter the width of rectangle {i}: "))
    lengths.append(length)
    widths.append(width)

print("\nNum\tLength\tWidth\t\tArea (approx.)")
for i in range(num_rectangles):
    area = calculate_area(lengths[i], widths[i])
    print(f"{i+1}\t{lengths[i]}\t{widths[i]}\t\t{area}")
