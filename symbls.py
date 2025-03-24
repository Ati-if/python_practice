rows = input("Enter the number of rows:")
columns = input("Enter the number of columns:")
symbol = input("Enter the symbol to be used:")



for x in range(int(rows)):
    for y in range(int(columns)):
      print(symbol , end = " ")
    print()