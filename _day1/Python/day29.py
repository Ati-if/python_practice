z = [0]*100
for i in range(0,10):
    print (z)





stg1 = "Hello"
stg2 = "World"
stg3 = stg1 + " " + stg2
print(stg3)





stg1 = "Hey"
stg2 = "there"
stg3 = "All"
stg = " {} {} , {}! ".format(stg1, stg2, stg3)
print(stg)





from array import *
arr = array('i' , [1,2,3,4,5])
print (arr)





print(arr.buffer_info())
print(arr[2])






for i in arr :
  print(i)






  for pnt in range(5):
   print(pnt , arr[pnt])