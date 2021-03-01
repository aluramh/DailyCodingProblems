class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


school_bus = Bus("School Volvo", 12, 50)
moto = Motorcycle("Mi moto", 100, 1)

# use Python's built-in isinstance() function
print(isinstance(school_bus, Vehicle))
print(isinstance(moto, Vehicle))
print(isinstance(moto, Bus))
