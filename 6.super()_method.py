# Super() method is used to access methods of the parent class

class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):

    def __init__(self, brand, type):
        super().__init__(type) # calling the type attribute from the parent class constructor
        self.brand = brand
        super().start()


car1 = Toyota('SUV', 'electric')
print(car1.type)