class Animal:
  alive = True


class Dog(Animal):
  def speak(self):
    print("Woof")

class Cat(Animal):
  def speak(self):
    print("Meow")

class Duck(Animal):
  def speak(self):
    print("Quack")

animals = [Dog(), Cat(), Duck()]

for animal in animals:
  animal.speak()
  print(animal.alive)