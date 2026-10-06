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











name = input("Enter the name of the student :")


marks = int(input("Enter the marks for subject 1 :"))
marks = int(input("Enter the marks for subject 2 :"))
marks = int(input("Enter the marks for subject 3 :"))

total = marks + marks + marks

percentage = total / 3


print("Student Name :" , name)
print("Total Marks :" , total)
print("Percentage :" , percentage)  


if percentage >= 90 :
    print("Grade : A")
elif percentage >= 80 :     
    print("Grade : B")
else :
    print("Grade : C")



if percentage >= 40 :
    print("Result : Pass")
else :
    print("Result : Fail")










price1 = float(input("Enter the price of item 1 :"))
price2 = float(input("Enter the price of item 2 :"))
price3 = float(input("Enter the price of item 3 :"))


total_price = price1 + price2 + price3

print("Total Price of the items is :" , total_price)












price = float(input("Enter the price of the product :"))

discount = price * 1

final_price = price - discount

print("Final Price after discount is :" , final_price)

print("Discount applied is :" , discount)