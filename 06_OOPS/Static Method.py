# Add a static method to the car class that returns a general description of a car

# Static Method -> method that belongs to a class rather than an instance of class
# to access static method use -> ClassName . method

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