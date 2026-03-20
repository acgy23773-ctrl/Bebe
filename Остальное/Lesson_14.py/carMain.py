from car import *

car1 = Car("Lada Granta", "Black", 200)

car1.printInfo()

name =getattr(car1, "name")
print(name)

setattr(car1, "color", "White")
car1.printInfo()
car1.start_engine()
car1.start_engine()
car1.stop_engine()
car1.stop_engine()