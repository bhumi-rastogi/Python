# ques -> add a method to car class that displays full name of car (brand and model)

class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        #attribute = #parameter
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"

    


my_car = Car("Toyota",'Corolla')
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())

my_new_car = Car("Tata","Safari")
print(my_new_car.model)