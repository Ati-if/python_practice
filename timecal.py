import time

my_time = int(input("Enter the time in seconds"))
for x in reversed(range (my_time , 0 , -1)):
  seconds = x % 60
  minutes = int(x / 60) % 60
  hours = int(x / 3600)
  print(f"{hours :02}:{minutes :02}:{seconds :02}")
  print(x)
  time.sleep(3)

print("Your time to sleep is up!")