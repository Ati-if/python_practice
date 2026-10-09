print("This is Atif , day44 of python practice .")






print("Testing my skills in python language .")









for number in range(2 , 51) :
    even = True

    for i in range(2 , number) :
        if number % 2 != 0 :
            even = False
            break

    if even :
        print(number)








for i in range(5) :
    print("You took the heart that begged for love and taught it how to hate")












total = 0

for i in range(1 , 51) :
    if i % 2 == 0 :
        total += i

print("The sum of the numbers is :" , total)











numbers = [10 , 20 , 30 , 40 , 10 , 20 , 20]

number = int(input("Enter number to count :"))

count = numbers.count(number)

print("Count :" , count)













def add(a , b) :
    return a + b

def subtract(a , b) :
    return a - b

def multiply(a , b) :
    return a * b 

def divide(a , b) :
    return a / b



a = int(input("Enter the first number :"))

b = int(input("Enter the second number :"))



print("Additon :" , add(a , b))
print("Substraction :" , subtract(a , b))
print("Multiplication :" , multiply(a , b))
print("Division :" , divide(a , b))









def check_even_odd(number) :
    if number % 2 == 0 :
        return "Even"

    else :
        return "Odd"


number = int(input("Enter a number :"))

print(check_even_odd(number))









number = int(input("Enter a number :"))

root = int(number * 1.5)

if root * root == number :
    print("Perfect Square")

else :
    print("Not a Perfect Square")










numbers = [10, -5, 20, -8, 0, 15, -3]


positive = 0
negative = 0



for number in numbers :
    if number > 0 :
        positive += 1
    elif number < 0 :
        negative += 1


print("Positive numbers are :" , positive)
print("Negative numbers are :" , negative)













numbers = [1 , 2 , 3 , 4 , 5]

reverse = []

for number in numbers :
    reverse.insert(0 , number)


print(reverse)









list1 = [1 , 2 , 3 , 4 , 5]
list2 = [2 , 3 , 4 , 6 , 5]


for number in list1 :
    if number not in list2 :
        print(number)










numbers = [10 , 20 , 10 , 20 , 30 , 40]

unique = []

for number in numbers :
    if number not in unique :
        unique.append(number)


print(unique)













sentence = input("Enter a sentence :")

words = sentence.split()

print("Numbers of words in sentence are :" , len(words))