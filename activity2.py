class Entity:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Entity):
    def move(self):
        return "The dog runs on four legs. 🐕"

class Fish(Entity):
    def move(self):
        return "The fish swims in water. 🐟"

class Car(Entity):
    def move(self):
        return "The car drives on roads. 🚗"

class Plane(Entity):
    def move(self):
        return "The plane flies in the sky. ✈️"

# Create objects
entities = [Dog(), Fish(), Car(), Plane()]

# Test polymorphism
for entity in entities:
    print(entity.move())
