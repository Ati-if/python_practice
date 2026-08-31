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







numbers = [5, 10, 15, 20, 25]

total = 0

for number in numbers:
    total += number

print("Total =", total)








marks = [70, 80, 65, 90, 75]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Average =", average)






numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even)
print("Odd =", odd)




numbers = [-5, 10, -2, 20, 15, -8]

for number in numbers:
    if number > 0:
        print(number)






numbers = [-5, 10, -2, 20, 15, -8]

for number in numbers:
    if number < 0:
        print(number)