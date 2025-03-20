unit = input("Is this temperature in celsius or fahrenheit")
temp = float(input("Enter the temperature"))

if unit == "celsius":
  temp = round(temp * 9/5 ) + 32 ,2
  print("The temperature in fahrenheit is {temp}")
elif unit == "fahrenheit":
  temp = round(temp - 32) * 5/9 ,3
  print("The temperature in celsius is {temp}")
else:
  print("Invalid unit")
  unit = "celsius"