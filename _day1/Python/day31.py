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