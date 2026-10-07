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