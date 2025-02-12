# polymorphism -> joh anek rup dharan kar sake

# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours

class Car:
    def __init__(self,brand,model):
        self.__brand = brand 
        #attribute = #parameter
        self.model = model

    def get_brand(self):
        return self.__brand + ' !'
    
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car): #inherits all the properties of car
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85kWh")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())

safari = Car("Tata","Safari")
print(safari.fuel_type())