print("Hello, World!")






number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse =", reverse)









def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", add(a, b))
print("Subtraction =", subtract(a, b))
print("Multiplication =", multiply(a, b))
print("Division =", divide(a, b))








def square(number):
    return number * number


number = int(input("Enter number: "))

print("Square =", square(number))