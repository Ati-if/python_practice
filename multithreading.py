import threading
import time

def walk_dog(first):
  time.sleep(5)
  print("You finished walking {first}")

def take_out_trash():
  time.sleep(2)
  print("You take out the trash from the street")

def get_email():
  time.sleep(3)
  print("You get your email")

walk_dog("Scooby")
take_out_trash()
get_email()

chore1 = threading.Thread(target=walk_dog , args=("Scooby",))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_email)

chore1.start()
chore2.start()
chore3.start() 

chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")