# Inheritance = means child class having access to all the attributes or methods found in the
#               parent class. So we don't need to write the code again n again

class Car:

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped")

# -----------------------------------------------------------------------------

# this is single inheritance
class Toyota(Car): # we inherited everything from the class 'Car'

    def __init__(self, brand):
        self.brand = brand

# -----------------------------------------------------------------------------

# this is multi-level inheritance
class Fortuner(Toyota): # we inherited everything from the class 'Toyota'

    def __init__(self, type):
        self.type = type

product = Fortuner("diesel")
product.start() # inheriting start() method directly from the great parent class 'Car'

# -----------------------------------------------------------------------------

# this is multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class meeting(A, B): # inheriting everything from both classes A and B
    meet = "welcome to meeting!"

meeting = meeting()
print(meeting.varA)
print(meeting.varB)
print(meeting.meet)