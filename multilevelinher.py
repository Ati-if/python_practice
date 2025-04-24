class Animal:
  def eat(self):
    print(f"{self.name} is eating")

  def sleep(self):
    print(f"{self.name} is sleeping")  
  
  def __init__(self, name):
    self.name = name

class Prey(Animal):
  def flee(self):
    print(f"{self.name} is fleeing")

class Predator(Animal):
  def hunt(self):
    print(f"{self.name} is hunting")

class Rabbit(Prey):
  pass

class Falcon(Predator):
  pass

class Fish(Prey , Predator):
  pass

rabbit = Rabbit("Bugs")
falcon = Falcon("Tony")
fish = Fish("Nemo") 

rabbit.flee()
falcon.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
rabbit.sleep()
falcon.eat()
falcon.sleep()
fish.eat()
fish.sleep()