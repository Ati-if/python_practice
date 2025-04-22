class student:
   

   class_year = 2024
   num_students = 0

   def __init__(self, name, age):
    self.name = name
    self.age = age
    student.num_students += 1

student1 = student("Spongebob", 30)
student2 = student("Jack", 20)
student3 = student("Patrick", 25)
student4 = student("Sandy", 22)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
print(student3.name)
print(student3.age)
print(student4.name)
print(student4.age)
print(student1.class_year)
print(student2.class_year)
print(student3.class_year)
print(student4.class_year)
print(student.num_students)
print(f"My graduating class of {student.class_year} has {student.num_students} students")