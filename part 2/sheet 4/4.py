def convert_weight():
    for _ in range(5):  # Execute the program 5 times
        try:
            weight = float(input("Enter the weight: "))
            if weight < 0:
                print("Error: Invalid weight. Weight cannot be negative.")
                continue

            unit = input("Enter the unit (mg, Kg, Ton): ").lower()

            if unit == 'mg':
                gram = weight / 1000
                print(f"{weight} mg is equal to {gram} grams.")
            elif unit == 'kg':
                gram = weight * 1000
                print(f"{weight} Kg is equal to {gram} grams.")
            elif unit == 'ton':
                gram = weight * 1e6
                print(f"{weight} Ton is equal to {gram} grams.")
            else:
                print("Error: Invalid unit. Please enter mg, Kg, or Ton.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    convert_weight()
