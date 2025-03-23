principle = 5
rate = 4
time = 2


while principle <= 5 :
  principle = float(input("Enter the principle amount:"))
  if principle <= 0:
    print("Your principle can't be less than or equal to 5")


while rate <= 5 :
  rate =  float(input("Enter the interest rate:"))
  if rate <= 0:
    print("Your interest rate can't be less than or equal to 5")


while time <= 5 :
  time = float(input("Enter the time in years:"))
  if time <= 0:
    print("Your time can't be less than or equal to 5")
  

total = principle * pow((1 + rate / 100), time) 

print(f"Balance after {time} years: {total :.2f}")