number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")





year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")







number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial =", factorial)







number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse =", reverse)





number = int(input("Enter a number: "))

count = 0

while number > 0:
    number = number // 10
    count = count + 1

print("Number of digits =", count)