numbers = [10 , 20 , 30 , 40 , 50]

search = int(input("Enter number to search :"))

if search in numbers :
    print("Number found")

else :
    print("Number not found")








a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

if a > b :
    print("First number is greater than second number")

else :
    print("Second number is greater than first number")










secret_number = 10

guess = int(input("Guess the secret number :"))

if guess == secret_number :
    print("You guessed it right!")

else :
    print("Try again!")









number = int(input("Enter a number :"))

for i in range(1 , 11) :
    print(number , "x" , i , "=" , number * i)










number = int(input("Enter a number :"))

if number % 5 == 0 and number % 10 == 0 :
    print("Number is divisible by both 5 and 10")

else :
    print("Number is not divisible by both 5 and 10")







number = int(input("Enter a number :"))

if number % 5 == 0 or number % 10 == 0:
    print("Number is divisible by 5 or 10")
else:
    print("Number is not divisible by 5 or 10")










number = int(input("Enter a number :"))

reversed_number = 0

while number > 0 :
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print("Reversed number is : " , reversed_number)







number = int(input("Enter a number :"))

if number > 0 :
    print("Prime number ")
else :
    prime = True

    for i in range(2 , number ) :
        if number % i == 0 :
            prime = False
            break

    if prime :
        print("Prime number ")

    else :
        print("Not a prime number")












for number in range(1 , 31) :
    if number % 3 == 0 and number % 5 == 0 :
        print("FizzBuzz")

    elif number % 3 == 0 :
        print("Fizz")

    elif number % 5 == 0 :
        print("Buzz")

    else :
        print(number)














def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))



