menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart  = {}
total = 0.0

print("--- Shop Menu ---")
for number, (name, price) in menu.items():
    print(f"{number}. {name:<10} ${price:.2f}")
print("5. Done")

while True:
    choice = int(input("\nChoose an item (1-5): "))
    
    if choice == 5:
        break
    
    if choice in menu:
        name, price = menu[choice]
        quantity = int(input(f"How many {name}s? "))
        
        if name in cart:
            cart[name] += quantity
        else:
            cart[name] = quantity
        
        total += price * quantity
    else:
        print("Invalid choice, try again.")

print("\n--- Receipt ---")
for item, qty in cart.items():
    print(f"{item} x{qty}")

print(f"Total: ${total:.2f}")
print("Thank you!")