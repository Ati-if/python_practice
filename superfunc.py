class Shape:
  def __init__(self, colour, filled):
    self.colour = colour
    self.filled = filled

class Circle(Shape):
  def __init__(self, radius, colour, filled):
    self.radius = radius
    super().__init__(colour, filled)

  def get_area(self):
    return 3.14 * self.radius ** 2

class Triangle(Shape):
  def __init__(self, base, height, width, colour, filled):
    self.base = base
    self.height = height
    self.width = width
    super().__init__(colour, filled)

  def area(self):
    return 0.5 * self.base * self.height

class Square(Shape):
  def __init__(self, side, width, filled, colour):
    self.side = side
    self.width = width
    super().__init__(colour, filled)
  def area(self):
    return self.side ** 2


circle = Circle(radius = "10", colour =  "Red", filled =  "True")
print(circle.colour)
print(circle.radius)
print(circle.filled)

triangle = Triangle(base = "10", height = "10", width = "10", colour = "Red", filled = "True")
print(triangle.colour)
print(triangle.base)
print(triangle.height)
print(triangle.width)
print(triangle.filled)

square = Square(side = "10", width = "10", filled = "True", colour = "Red")
print(square.colour)
print(square.side)
print(square.width)
print(square.filled)