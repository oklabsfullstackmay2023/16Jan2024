#1 class defination is one time process
class VehicleClass():
    #1. property/variable
    mileage=""
    pass
class Bus(VehicleClass):
    #2. constructor/esp.function
    def __init__(self,m):
        self.mileage=m
        pass
    pass

class Car(VehicleClass):
    #2. constructor/esp.function
    def __init__(self,m):
        self.mileage=m
        pass

class Truck(VehicleClass):
    #2. constructor/esp.function
    def __init__(self,m):
        self.mileage=m
        pass
    pass

#2. create class external object is many time process
bus1=Bus(5)
print(f'The mileage of bus is {bus1.mileage}')
 

car1=Car(26)
print(f"The mileage of car is {car1.mileage}")

truck1=Truck(3)
print(f'The mileage of truck is {truck1.mileage}')