# Modify the car class to encapsulate brand attribute, making it private, and provide a getter method for it

# encapsulate meaning capsule ka andar joh h wooh mera chanhe p hi apko pta lga

class Car:
    def __init__(self,brand,model):
        self.__brand = brand 
        #attribute = #parameter
        self.model = model

    def get_brand(self):
        return self.__brand + ' !'
    
    def fullName(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car): #inherits all the properties of car
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85kWh")
# print(my_tesla.__brand)
print(my_tesla.get_brand())


# __ variablename : it can accesseb by class but not by object