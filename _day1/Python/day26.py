import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
plt.show()





from array import *
arr = array("i" , [])
x = int(input("Enter the size of array"))
print("Enter %d elements" %x)
for i in range(x):
  x = int(input("Enter the next value"))
  arr.append(x)
  print(arr)




def add (a , b) :
   total = a + b
   print("The sum is : " , total)

add(20 , 30)

x = 30
y = 50

add(x , y)






class Person :
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def talk(self) :
    print("Hi, I am ", self.name)

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.talk()







class Person :
  def __init__(self):
    self.name = "Sam"
    self.gender = "Male"
    self.age = 24 # Store age as an integer
  def talk(self) :
    print("Hi, I am ", self.name)
  def vote(self) :
    if self.age <= 15 : # Access age attribute correctly
      print("I am not eligible to vote")
    else:
      print("I am eligible to vote")

obj = Person()
obj.talk()
obj.vote()