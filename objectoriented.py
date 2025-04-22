class Car:
  def __init__(self, make, model, year, colour, for_sale):
    self.make = make
    self.model = model
    self.year = year
    self.colour = colour
    self.for_sale = for_sale

carBMW = Car("Mustang", "xyz", 2024, "red", False)
carTOYOTA = Car("Corolla", "abc", 2023, "black", True)

print(carBMW.make)
print(carBMW.model)
print(carBMW.year)
print(carBMW.colour)
print(carBMW.for_sale)


print(carTOYOTA.make)
print(carTOYOTA.model)
print(carTOYOTA.year)
print(carTOYOTA.colour)
print(carTOYOTA.for_sale)