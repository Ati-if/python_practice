temp = 20
is_sunny = "true"

if temp >= 20 and  not is_sunny:
  print("It is SUNNY day")
  print("It is hot outside")

elif temp <= 5 and not is_sunny:
  print("It is COLD day")
  print("It is cold outside")

elif 20 > temp > 5 and not is_sunny:
  print("It is RAINY day")
  print("It is not safe outside")

else:
  print("Invalid input")