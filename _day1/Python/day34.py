print("Hello MR . Atif")


a = float(input("Enter the first number :"))
b = float(input("Enter the second number :"))

print("The sum of two numbers is : " , a + b)

print("The difference of two numbers is :" , a - b)

print("The product of two numbers is :" , a * b)

print("The division of two numbers is :" , a / b)






name = input("Enter your name :")
age = int(input("Enter your age :"))

print("Hello" , name , "You are" , age , "years old")

print(f"Hello, {name}\nYou are {age} years old")






number = int(input("Enter a number :"))

for i in range(1 , 11) :
    print(number , "x" , i , "=" , number * i)