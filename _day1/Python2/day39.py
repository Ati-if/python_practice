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