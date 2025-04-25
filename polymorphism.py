from abc import ABC , abstractmethod

class Shape:
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius ** 2

class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2

class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5 * self.base * self.height

class Pizza(Circle):
  def __init__(self, radius, toppings):
    super().__init__(radius)
    self.toppings = toppings

shapes  = [Circle(radius=5), Square(side=6), Triangle(base=4, height=6), Pizza(radius=8, toppings=["Cheese", "Pepperoni"])]

for shape in shapes:
  print(shape.area())