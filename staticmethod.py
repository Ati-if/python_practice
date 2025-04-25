class Employee:


  def __init__(self, name, position):
    self.name = name
    self.position = position

  def get_info(self):
    return f"{self.name} = {self.position}"


  @staticmethod
  def is_valid_position(position):
    valid_positions = ["Manager", "Developer", "Tester"]
    return position in valid_positions

employee1  = Employee("John", "Manager")
print(employee1.get_info())
employee2 = Employee("Jane", "Developer")
print(employee2.get_info())
employee3 = Employee("Jack", "Tester")
print(employee3.get_info())
print(Employee.is_valid_position("Tester")) 