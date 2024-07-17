# Abstraction: Hiding the implementation details of a class and only showing the essential
# features to the user.
# For e.g:

class Car:

    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car Started!") # only necessary detail

car1 = Car()
car1.start()
# when we print this, we see the car started
# but, we don't get to see the internal process
# like how the clutch, accelerator and brake were False before but when we start the car
# we made them True. That's all unnecessary details that are not supposed to be shown
# to the user. That is Abstraction

# Encapsulation: wrapping the data and functions into a single unit(object)
# everything that we do in classes like making functions in it, putting in data and attributes
# we're actually putting all functions and data into a capsule(class) and encapsulating it
# and making it all one single unit. That is called Encapsulation
