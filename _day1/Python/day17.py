numbers = [15, 8, 42, 23, 10]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest =", largest)





numbers = [15, 8, 42, 23, 10]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest =", smallest)