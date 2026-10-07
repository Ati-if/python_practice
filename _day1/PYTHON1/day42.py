print("Hello World, This is day 42 of Python programming!")






print("This is Atif Nawaz , I am learning python")









number = int(input("Enter a number :"))

if number % 2 == 0 :
    print("The number is even")

else :
    print("The number is odd")










number = int(input("Enter a number : "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)











year = int(input("Enter a year :"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")

else :
    print(year, "is not a leap year")













numbers = [10 , 20 , 30 , 40 , 50 , 60]

smallest = min(numbers)

for number in numbers :
    if number < smallest :
        smallest = number


print("The smallest number in the list is :", smallest)










numbers = [10 , 20 , 30 , 40 , 50 , 60]

largest = max(numbers)

for number in numbers :
    if number > largest :
        largest = number


print("The largest number in the list is :" , largest)










numbers = [10 , 15 , 17 , 20 , 23 , 25 , 30]

count = 0 

for number in numbers :
    if number % 2 == 0 :
        count += 1


print("The count of even numbers in the list is :" , count)










numbers = [10 , 15 , 17 , 20 , 23 , 25 , 30]

count = 0 

for number in numbers :
    if number % 2 != 0 :
        count += 1 


print("The count of odd numbers in the list is :" , count)











a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a // b)