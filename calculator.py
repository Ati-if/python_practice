operator = input("Enter an operator (+  -  *  / )")

num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)



num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

operator = input("Enter an operator (+  -  *  / )")


if operator  == "+":
  result = num1 + num2
  print(result)
elif operator == "-":
  result = num1 - num2
  print(result)
elif operator == "*":
  result = num1 * num2
  print(result)
elif operator == "/": 
  result = num1 / num2
  print(result)