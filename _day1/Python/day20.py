number = int(input("Enter a number: "))

original = number
total = 0

while number > 0:
    digit = number % 10
    total = total + digit ** 3
    number = number // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")