number = int(input("Enter a number: "))

if number % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")







a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

numbers = [a, b, c]
numbers.sort()

print("Middle number =", numbers[1])








for i in range(1, 11):
    print(i, "=", i * i * i)