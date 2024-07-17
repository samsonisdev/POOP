# Private(like) attributes and methods
# Private attributes and methods are meant to be used only within the class and are not
# accessible from outside the class

# For e.g:
# An example of Public attributes and methods where we can access the attributes and methods
# that were inside the class scope. That means they are public
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("Hello", self.name)

s1 = Student("Samson", 99)
print(s1.name)
s1.hello()

# An example of Private attributes and methods where we cannot access the attributes and methods
# that were inside the class scope. That means they are private and won't be displayed.
# To make an attribute or method private, we add __ before the name of attribute or method

class Account:

    def __init__(self, account_no, password):
        self.account_no = account_no
        self.__password = password # private attribute

    def __hello(self): # private method
        print("Hello world!")

    def welcome(self):
        self.__hello()

acc1 = Account(222, "sayy")
# print(acc1.password) # we can't access password as it's a private attribute now
# acc1.__hello() # again we can't access hello() as it's a private method now
acc1.welcome() # but by putting __hello() into another method, we can access __hello()
#                but can't access it directly
