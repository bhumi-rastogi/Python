# Add a static method to the car class that returns a general description of a car

# Static Method -> method that belongs to a class rather than an instance of class
# to access static method use -> ClassName . method
# isme self nhi likhna

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
    
    @staticmethod #decorators-> methods ki functionality ko enhance kar dete h
    def general_description():
        return "Cars are means of transport"
    
my_car = Car("Tata","Safari")
# print(my_car.general_description())
print(Car.general_description())