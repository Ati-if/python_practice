number = int(input("Enter a number: "))

root = int(number ** 0.5)

if root * root == number:
    print("Perfect square")
else:
    print("Not a perfect square")





numbers = [10, -5, 20, -8, 0, 15, -3]

positive = 0
negative = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)



numbers = [10, 50, 20, 40, 30]

numbers.sort()

print("Second largest =", numbers[-2])





numbers = [1, 2, 3, 4, 5]

reverse = []

for number in numbers:
    reverse.insert(0, number)

print(reverse)




list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

for number in list1:
    if number in list2:
        print(number)