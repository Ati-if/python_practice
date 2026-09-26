import numpy as np

# Create NumPy array
marks = np.array([78, 85, 92, 67, 88])

# Display original array
print("Original Array:")
print(marks)

# Convert array to float data type
marks_float = marks.astype(float)

# Display converted array
print("\nConverted Array:")
print(marks_float)






celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit =", fahrenheit)





fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Celsius =", celsius)





principal = float(input("Enter the principal amount :"))
rate = float(input("Enter the rate of interest :"))
time = float(input("Enter the time in years :"))

interest = (principal * rate * time) / 100

print("Simple Interest = " , interest)





print("1 : Say Hello")
print("2 : Say Goodbye")
print("3 : Exit")

choice = int(input("Enter your choice :"))

if choice == 1:
    print("Hello!")
elif choice == 2:
    print("Goodbye!")
elif choice == 3:
    print("Exiting...")
else:
    print("Invalid choice!")




number = int(input("Enter a number "))
if number % 10 == 0 :
    print("The number is divisible by 10")
else :
    print("The number is not divisible by 10")