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




class Car :
    def __init__ (self , year , speed , model) :
        self.year = year 
        self.speed = speed
        self.model = model
    def getspeed(self) :
        print("The speed of the car is :" , self.speed , "km/h")

BMW = Car(2020 , 150 , "BMW X5")
BMW.getspeed()
Ford = Car(2021 , 200 , "Ford Mustang")
Ford.getspeed()
def getspeed(self) :
    print("The speed of the car is :" , self.speed , "km/h")










class Sedan(Car) :
    def accelerate(self) :
        print("150 km/h to 200 km/h in 5 seconds")

    def openroof(self) :
        print("The roof is open")

class SUV(Car) :
    def accelerate(self) :
        print("100 km/h to 150 km/h in 10 seconds")

    def openroof(self) :
        print("The roof is closed")


BMW.getspeed()

Honda = Sedan(2022 , 150 , "Honda Accord")
Honda.getspeed()
Honda.accelerate()
Honda.openroof()

Ford = SUV(2021 , 200 , "Ford Mustang")
Ford.getspeed()
Ford.accelerate()
Ford.openroof()
