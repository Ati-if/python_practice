menu = {
    "Pizza": 3.00,
    "Burger": 2.90,
    "Fries": 2.80,
    "Popcorn": 6.90,
    "Soda": 2.00
}

cart = []
total = 0

print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:8} : ${value:.2f}")
print("------------------------")

while True:
    food = input("Enter the food you want to buy (q to quit): ").title()  
    if food == "Q":
        break  
    if food in menu:
        cart.append(food)  
        print(f"{food} added to cart.")
    else:
        print("Item not found in menu. Please try again.")

print("\nItems purchased:", end=" ")
for food in cart:
    total += menu.get(food, 0) 
    print(food, end=" ")

print(f"\nTotal: ${total:.2f}") 