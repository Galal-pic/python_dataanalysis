available_items = {'Meat': 0, 'Seafood': 0, 'Milk': 0, 'Bread': 0, 'Oil': 0}
prices = {'Meat': 0, 'Seafood': 0, 'Milk': 0, 'Bread': 0, 'Oil': 0}

for department in available_items:
    available_items[department] = int(input(f"How many available items in {department}? "))
    
for department in prices:
    prices[department] = float(input(f"What are the prices of the available items in {department}? "))

total_sold_items = 0
ratios = {}

while True:
    order = {}
    
    for department in available_items:
        order[department] = int(input(f"How many do you want from {department}? "))
        
    promo_code = input("Please enter promo if you have: ")
    
    total = 0
    for department in available_items:
        if order[department] > available_items[department]:
            print(f"We are sorry, there's no available {department}")
            continue
        total += order[department] * prices[department]
    
    if promo_code == '123456' and order['Milk'] > 0:
        total *= 0.7  # Apply a 30% discount on Milk
    
    print(f"Dear prospective customer, the total is: {total:.1f} pounds")
    
    total_sold_items += sum(order.values())
    for department in order:
        if department not in ratios:
            ratios[department] = 0
        ratios[department] += order[department] / total_sold_items
    
    is_open = input("Is the store still open? (yes/no) ").lower()
    if is_open == 'no':
        break

print("We sold today:")
for department, ratio in sorted(ratios.items(), key=lambda x: x[1]):
    print(f"{ratio*100:.2f}% {department}")
