temp = 6
is_sunny = "false"

if temp >= 20 and is_sunny:
  print("It is SUNNY day")
  print("It is hot outside")

elif temp <= 5 and is_sunny:
  print("It is COLD day")
  print("It is cold outside")

elif 20 > temp > 5 and is_sunny:
  print("It is RAINY day")
  print("It is not safe outside")

else:
  print("Invalid input") 