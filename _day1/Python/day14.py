principal = float(input("Enter principal: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))

interest = (principal * rate * time) / 100

print("Simple Interest =", interest)






student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])





student = {
    "name": "Ali",
    "age": 20
}

student["marks"] = 85

print(student)