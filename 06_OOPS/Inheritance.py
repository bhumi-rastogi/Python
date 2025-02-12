# Create an ElectricCar class that inherits from the Car class and has an additional attribute

class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        #attribute = #parameter
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car): #inherits all the properties of car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.brand)
print(my_tesla.fullName())