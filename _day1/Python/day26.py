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