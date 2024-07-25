class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type) #---> super() method used to call parent's method
        self.name = name
car1 = ToyotaCar("Toyota","Electric")
car1.start()
car1.stop()
print(car1.name)
print(car1.type)