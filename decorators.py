def add_sprinkles(func):
  def wrapper():
    print("Adding sprinkles✨")
    func()
  return wrapper

@add_sprinkles
def add_chocolate():
  print("Adding chocolate🍫")

add_chocolate()

def add_fudge(func):
  def wrapper():
    print("Adding fudge🍫")
    func()
  return wrapper

@add_sprinkles
def add_Brownie():
  print("Adding Brownie🍪")

add_Brownie() 



def get_ice_cream():
  print("Here is your ice cream🍦🍫,🍪🍦")

get_ice_cream()