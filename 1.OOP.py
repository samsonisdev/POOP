# OOP (Object-Oriented Programming) = By OOP we can create representation of real life objects by assigning classes.
# Classes are like a blueprint for objects
# An object has two main things:
# 1) Data/Attribute = Features of an object like a watch's shape, color, material, etc.
# 2) Methods/Functions = Things that an object can do, like a watch can show time, change time etc

# __init__ is a constructor that runs by default even if we use it or not.
# The self parameter is a reference to the current instance(object) of the class
# and is used to access variables that belongs to the class.
# self parameter points towards the object.
# For e.g if we print(self) or if we print(s1), we'll get the same output
# In the below example, every student's name and marks will be different
# so, we used self.name, self.marks. But if attribute would be same for every student
# like university name then we will use the variable without self outside the constructor
# Because objects occupy space in memory

class Student:
    university = "SMIU" # class attribute
    name = "anonymous"

    # constructor
    def __init__(self, full_name, marks):
        self.name = full_name # object attribute
        self.marks = marks
        # print(self)

    # methods
    def welcome(self):
        print("Hey welcome", self.name)

    def get_marks(self):
        return self.marks

# print(s1)
s1 = Student("Samson", 94)
s1.welcome()
print(s1.get_marks())

# when we print the constant thing that is same for all objects
# like university name:
print(s1.university)
# we can also call it like:
print(Student.university)
# but as we have two same variables. name and self.name
# When we say s1.name what should be printed?
print(s1.name) # the name that is entered in the object will pe printed
# so to call the name variable that stores "anonymous"
# we will call the class name Student.name because here name is a class attribute
print(Student.name)
# So, object attributes has higher preference than class attributes
# But normally we don't use the same names for class attribute and object attribute

# we can delete an object, or it's attribute by using 'del' keyword
del s1.name
del s1