name = input("Enter your name")

while name ==  "":
  print("You did not enter your full name")
  name = input("Enter your name")

print(f"Hello {name}")



food = input("Enter your favourite food (q to quit):")

while not food ==  "q":
  print(f"You like {food}")
  food = input("Enter your favourite food (q to quit):")

print("Good Bye")  