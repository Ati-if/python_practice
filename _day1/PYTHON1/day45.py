print("This is my final day")






print("From Tomorrow, I shall start matplotlib by creating a new repository.")









numbers = [50 , 20 , 30 , 60 , 10 , 40]

numbers.sort()

print("Second largest number is :" , numbers[-3])









numbers = [1 , 2 , 3 , 4 , 5 , 10]

reverse = []

for number in numbers :
    reverse.insert(0 , number)


print(reverse)











list1 = [1 , 2 , 3 , 4 , 5]
list2 = [3 , 4 , 5 , 6 , 7]

for number in list1 :
    if number in list2 :

        print(number)









numbers = [10 , 20 , 20 , 10 , 30 , 20 , 40 , 50]


unique = []

for number in numbers :
    if number not in unique :
        unique.append(number)


print(unique)









import numpy as np

marks = np.array([78 , 85 , 95 , 50 , 60])

print("Original Array :")
print(marks)

marks_float = marks.astype(float)


print("\n Converted Array :")
print(marks_float)










a = int(input("Enter the value of a :"))

b = int(input("Enter the value of b :"))

a , b = b , a

print("a = " , a)
print("b = " , b)


