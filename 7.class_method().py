# Class Method: is bound to the class and receives the class as an implicit first argument
# Note - static methods can't access or modify class state and generally for utility

# So, in the code below, we have two attributes with the same name 'name' and self.name
# (Read code)
# when we change the name, the name = 'anonymous' doesn't really change
# cuz in the method, changeName(), the method creates another attribute self.name
# which doesn't affect the class attribute 'name'

class Person:

    name = "anonymous" # class attribute

    def changeName(self, name):
        self.name = name

    # So, to change the class attribute 'name', we access the class attribute
    # For e.g:
    def change(self, name):
        Person.name = name

    # Another way to do the same thing
    # Here, __class__ is actually representing the class name 'Person'
    # So, Person.name OR __class__.name, it's the same thing
    def changing(self, name):
        self.__class__.name = name

    # But another way to do it with class method is creating the class method
    # which help us access class attribute directly
    @classmethod
    def changeThisName(cls, name):
        cls.name = name



per = Person()
per.changeThisName('Samson')
print(per.name)
print(Person.name)

