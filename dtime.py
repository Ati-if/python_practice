import datetime

date = datetime.date(2023, 1, 1)
today = datetime.date.today()
time = datetime.time(12, 30, 45)
now = datetime.datetime.now()

now_str = now.strftime("%Y-%m-%d %H:%M:%S")
target_datetime = datetime.datetime.strptime("2023-01-01", "%Y-%m-%d")
current_datetime = datetime.datetime.now()
time_difference = target_datetime - current_datetime

if target_datetime > current_datetime:
  print("Target date is in the future")
elif target_datetime < current_datetime:
  print("Target date is in the past")
else:
  print("Target date is today")

print(date)
print(today)
print(today.year)
print(today.month)
print(today.day)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(now)
print(now_str)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(target_datetime)
print(current_datetime)
print(time_difference)