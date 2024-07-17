# Practice Question 1:
# Create a student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        return round(avg, 2)

s1 = Student("Samson", 94, 78, 87)
print(s1.average())
s2 = Student("Jake", 45, 45, 66)
print(s2.average())

# we can also change the attribute
s1.name = "Rizz"
print(s1.name)
