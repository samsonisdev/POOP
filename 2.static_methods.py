# Static Methods: methods that don't use the self parameter
# For e.g:

class Student:

    def __init__(self, full_name, marks):
        self.name = full_name
        self.marks = marks

    # Here, we're just printing "Hello world!" that doesn't take any attributes inside it
    # so, there's no need to use the self parameter. But if we don't use the self parameter
    # the program will give error
    def hello(self):
        print("Hello world!")

    # so, to use a function without self parameter because there's no use of self
    # we use static methods

    @staticmethod # decorator
    def hello_user():
        print("Hello user!")

    def welcome(self):
        print("Hey welcome", self.name)

# Decorators allow us to wrap another function in order to extend the behavior
# of the wrapped function, without permanently modifying it

s1 = Student("samson", 98)
s1.hello_user()
