# question -> create a car class with attribute like model and brand. Then create an instance of this class.

class Car:
    def __init__(self,brand,model):
        self.brand = brand 
        #attribute = #parameter
        self.model = model
    


my_car = Car("Toyota",'Corolla')
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car.model)