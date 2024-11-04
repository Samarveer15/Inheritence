class Vehicle:


    def __init__(self, name, max_speed, milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

class bus(Vehicle):
    pass


School_bus = bus("School Valvo", 180, 12)
print("Vehicle Name:",School_bus.name, "Speed::", School_bus.max_speed,"Milage:",School_bus.milage)