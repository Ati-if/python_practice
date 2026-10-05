a = 0
b = 1

for i in range(10):
    print(a)
    a, b = b, a + b








def square(number) :
    return number * number

number = int(input("Enter a number :"))

print("Square of " , number , "is" , square(number))







import math

print("Square root of 25 is" , math.sqrt(25))









from math import sqrt

number = int(input("Enter a number :"))

print("Square root of" , number , "is" , sqrt(number))










total = 0

for i in range(1 , 15) :

    if i % 2 != 0 :

        total += i 

print("Sum of odd numbers from 1 to 15 is" , total)








fruits = ["Apple" , "Banana" , "Mango" , "Grapes"]

fruits.remove("Mango")

print(fruits)







fruits.append("Orange")

print(fruits)