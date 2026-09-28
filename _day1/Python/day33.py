age = int(input("Enter your age :"))
if age < 18 :
    print("You are a minor .")
elif age <= 25 :
    print("You are an adult .")
else :
    print("You are a senior citizen .")







number = int(input("Enter a number :"))
if number % 2 == 0 :
    print("The number is even . ")

else :
    print("The number is odd .")







year = int(input("Enter a year :"))
if year % 4 == 0 :
    print("The year is a leap year .")
else :
    print("The year is not a leap year .")







number = int(input("Enter a number :"))

factorial = 1 

for i in range(1 , number + 1) :
    factorial = factorial * i

print("The factorial of", number, "is", factorial)







number = int(input("Enter a number :"))

reverse = 0

while number > 0 :
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("The reverse of the number is :" , reverse)







number = int(input("Enter a number :"))


count = 0 

while number > 0 :
    number = number // 10
    count += 1


print("The number of digits in the number is :" , count)