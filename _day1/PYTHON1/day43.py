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