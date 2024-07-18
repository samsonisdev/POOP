# Practice Question 4:
# Define an Employee class with attributes: role, department, salary
# This class also defines the showDetails() method
# Create an Engineer class that inherits properties from Employee class
# and has additional attributes: name, age

class Employee:

    def __init__(self, role, dep, sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def show_details(self):
        print("Role:", self.role,
              "\nDepartment:", self.dep,
              "\nSalary:", self.sal)

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Construction", 45000)

    def showDetails(self):
        print("Name:", self.name,
              "\nAge:", self.age)

emp = Engineer("Samson", 40)
emp.show_details()
emp.showDetails()