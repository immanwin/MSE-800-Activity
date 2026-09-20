#Structural Pattern (Decorators)

class Car:
    def cost(self):
        return 25000
    def description(self):
        return "Basic Car"

#Base Decorator
class CarDecorator:
    def __init__(self,car):
        self.car = car

    def cost(self):
        return self.car.cost()

#Concrete Decorators
class GPSDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 500

class SunroofDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1000

class LeatherSeatsDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 1500

class PremiumSoundSystemDecorator(CarDecorator):
    def cost(self):
        return self.car.cost() + 800

car = PremiumSoundSystemDecorator(LeatherSeatsDecorator(SunroofDecorator(GPSDecorator(Car()))))
print(f"The Total Cost: ${car.cost()}")