password = input("Enter your password :")

if password == "1390" :
    print("Access granted")
else : 
    print("Access denied")








names = ["John", "Alice", "Bob", "Eve"]

print(names)
print(names[0])







secret = 7

while True :
    guess = int(input("Guess the secret number :"))
    if guess == secret :
        print("You guessed it right!")
        break
    else :
        print("Try again!")