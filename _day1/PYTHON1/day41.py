print("Hello  World!")








for i in range(5):
    print("This is iteration number:", i + 1)








def cube(number) :

    return number * number * number

number = input("Enter a number to find its cube :")

print("The cube of", number, "is", cube(int(number)))











numbers = [10 , 20 , 30 , 40 , 50 , 60]

total = 0 

for number in numbers :
    total += number


average = total / len(numbers)

print("The average of the numbers is :" , average)









numbers = [10 , 20 , 30 , 40 , 50 , 60]


numbers = [number * 2 for number in numbers ]

print("The doubled numbers are:" , numbers)











def check_even_odd(number) :

    if number % 2 == 0 :
        return "Even Number"

    else :
        return "Odd Number"


number = input("Enter a number to check if it is even or odd :")

print("The number", number, "is an", check_even_odd(int(number)))