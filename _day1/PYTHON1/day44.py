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


