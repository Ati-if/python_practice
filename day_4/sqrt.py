import math

a = int(input("Enter the value of side 'A'"))
b = int(input("Enter the value of side 'B'"))
c = int(input("Enter the value of side 'C'"))

d = math.sqrt(pow(a, 2) + pow(b, 2) + pow(c, 2))

print((f"The value of D is {d}"))



import math

a = int(input("Enter the value of side 'A'"))
b = int(input("Enter the value of side 'B'"))
c = int(input("Enter the value of side 'C'"))

d = math.sqrt(pow(a, 2) + pow(b, 2) + pow(c, 2))

print((f"The value of D is {round (d , 2)}"))


age = int(input("Enter your age"))

if age >= 18:
  print ("You are an adult")
elif age <= 18:
  print("You are not an adult person")
else:
  print("Invalid input")