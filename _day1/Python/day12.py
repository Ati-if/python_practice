total_sales = 0

for i in range(1, 6):
    sales = float(input(f"Enter sales amount for Employee {i}: "))

    if sales < 50000:
        tax = sales * 0.05
    elif sales <= 100000:
        tax = sales * 0.10
    else:
        tax = sales * 0.15

    print(f"Sales Amount: Rs. {sales:.2f}")
    print(f"Tax Amount: Rs. {tax:.2f}")
    print("-" * 30)

    total_sales += sales

average_sales = total_sales / 5

print("Total Sales: Rs.", round(total_sales, 2))
print("Average Sales: Rs.", round(average_sales, 2))




total_sales = 0

for i in range(1, 6):
    sales = float(input(f"Enter sales amount for Employee {i}: "))

    if sales < 50000:
        tax = sales * 0.05
    elif sales <= 100000:
        tax = sales * 0.10
    else:
        tax = sales * 0.15

    print(f"Sales Amount: Rs. {sales:.2f}")
    print(f"Tax Amount: Rs. {tax:.2f}")
    print("-" * 30)

    total_sales += sales

average_sales = total_sales / 5

print("Total Sales: Rs.", round(total_sales, 2))
print("Average Sales: Rs.", round(average_sales, 2))




