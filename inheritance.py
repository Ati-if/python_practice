class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.is_alive = True

  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")

class Dog(Animal):
  def __init__(self, name, breed, colour):
    super().__init__(name, species="Dog")
    self.breed = breed
    self.colour = colour
  def bark(self):
    print(f"{self.name} is barking")
  def speak(self):
    print(f"{self.name} says Woof!")

class Cat(Animal):
  def __init__(self, name, species, fur_colour):
    super().__init__(name, species)
    self.fur_colour = fur_colour
  
  def speak(self):
    print(f"{self.name} says Meow!")

class Mouse(Animal):
  def __init__(self, name, species, colour):
    super().__init__(name, species)
    self.colour = colour
  def speak(self):
    print(f"{self.name} says Squeek!")

dog = Dog("Scooby", "Dog", "White")
cat = Cat("Tom", "Cat", "Brown")
mouse = Mouse("Jerry", "Mouse", "Grey")

print(dog.name)
print(dog.species)
print(dog.breed)
print(dog.colour)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.bark()  
dog.speak()

