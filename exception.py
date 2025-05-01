try:
  number = input("Enter a number:")
  print(1 / int(number))
except ValueError:
  print("Invalid input")
except ZeroDivisionError:
  print("Cannot divide by zero")  
except Exception:
  print("Something went wrong")  
else:
  print("No exceptions were raised")
finally:
  print("This will always execute")