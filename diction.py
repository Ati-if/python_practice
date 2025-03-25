capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("China"))

if capitals.get("China"):
  print("That capital exists")
else:
  print("That capital does not exist")


for key, value in capitals.items():
  print(f"{key} : {value}")