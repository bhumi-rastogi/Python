# Add a class variable to Car that keeps track of the number of cars created

class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand 
        #attribute = #parameter
        self.model = model
        Car.total_car += 1 

    def get_brand(self):
        return self.__brand + ' !'
    
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

safari = Car("Tata","Safari")
safariThree = Car("Tata","Nexon")
print(safari.fuel_type())
print(safari.total_car)

# better way 
print(Car.total_car)
