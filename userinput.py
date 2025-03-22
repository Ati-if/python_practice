username = input("Enter a username")

if len(username) > 12:
  print("Your username can't have more than 12 characters")

else:
  print(f"Hello {username}")
  print(f"How are you {username}")