height = float(input("Enter your height"))
unit = input("Centimeter or meter")

if unit == "CM":
  height = height * 100
  unit = "CM"
elif unit == "M":
  height = height / 100
  unit = "M"
else :
  print(f"Your {unit} was not valid")

  print(f"Your height is: {height} {unit}")