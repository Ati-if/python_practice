import time
from datetime import datetime
from zoneinfo import ZoneInfo
import zoneinfo

now = datetime.now(ZoneInfo("Asia/Karachi"))

print("Current local time :" , now.strftime("%y-%m-%d %h:%M:%S %Z%z"))

epc = time.time()
print(epc)
localtime = time.localtime(epc)

print("Local current time :", time.asctime(localtime))





from threading import Thread
class Demo :
    def show(self) :
        for i in range(5) :
            print("Child Thread")
            time.sleep(1)

object = Demo()
t = Thread(target = object.show())
t.start()
for i in range(5) :
    print("Main Thread")
    time.sleep(1)







from threading import *
def show() :
    for i in range(4) :
        print("This is a child thread")


t = Thread(target = show)
t.start()
print("This is the main thread")






class Car :
    def  getspeed(self) :
        print("The speed of the car is 150 km/h")


BMW = Car()
BMW.getspeed()
