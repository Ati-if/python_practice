print("Hello, World!")






number = int(input("Enter some numbers :"))

if number > 0 :
    print(number , "is a positive number")

elif number < 0 :
    print(number , "is a negative number")

else :
    print(number , "is zero")










numbers = [10 , 20 , 30 , 40 , 50 , 60]

total = 0

for number in numbers :
    total += number


print("The sum of all numbers in the list is :" , total)











password = input("Enter a password :")

if len(password) < 5 :
    print("Password is too short")

elif len(password) > 10 :
    print("Password is too long")

else :
    print("Password is valid")









password = input("Enter a password :")

if password.isalnum() and len(password) >= 5 and len(password) <= 10 :
    print("Password is valid")

elif not password.isalnum() :
    print("Password should contain only letters and numbers")

else :
    print("Password should be between 5 and 10 characters long")











number = int(input("Enter a number :"))

factorial = 1

for i in range(1 , number + 1) :
    factorial *= i

print("The factorial of" , number , "is :" , factorial)









number = int(input("Enter a number :"))

count = 0 

while number > 0 :
    number // 10
    count += 1

print("The number of digits in the number is :" , count)