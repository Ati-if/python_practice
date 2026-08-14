numbers = [10, 25, 5, 40, 15]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest =", smallest)





numbers = [10, 15, 22, 31, 44, 50]

count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print("Even numbers =", count)






secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too small")
    else:
        print("Too large")








number = int(input("Enter a number: "))

if number < 2:
    print("Not prime")
else:
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not prime")








for number in range(2, 51):
    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number)






a = 0
b = 1

for i in range(10):
    print(a)
    a, b = b, a + b