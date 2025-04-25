class Student:

  count = 0
  total_gpa = 0

  def __init__(self, name, gpa):
    self.name = name
    self.gpa = gpa
    Student.count += 1
    Student.total_gpa += gpa

#INSTANCE METHOD
  def get_info(self):
    return f"{self.name} = {self.gpa}"

  @classmethod
  def get_count(cls):
    return f"Total # of students: {cls.count}"
  
  @classmethod
  def get_average_gpa(cls):
    if cls.count == 0:
      return 0
    else:  
     return f"Average GPA: {cls.total_gpa / cls.count}"

print(Student.get_count())
student1 = Student("John", 3.8)
print(student1.get_info())
student2 = Student("Jane", 3.9)
print(student2.get_info())
print(Student.get_count())
print(Student.get_average_gpa())
