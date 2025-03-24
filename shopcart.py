
prices = []
total = 0
foods = []

while True:
    food = input("Enter the food you like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("\nYOUR CART")
for food in foods:
    print(food)

for price in prices:
    total += price 

print(f"\nYour total price is: {total}") 