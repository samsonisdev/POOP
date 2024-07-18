# Polymorphism: Operator Overloading
# Poly means many, morph means forms
# When the same operator is allowed to have different meaning according to the context
# For e.g:

# Here + means
# print(1 + 2) # adding two numbers
# print("Samson" + "Rizz") # combining to strings
# print([1, 2, 3] + [4, 5, 6]) # merging two lists

# So, the + has different meanings according to the context/data types
# This is polymorphism when one thing has many forms according to the context

# Functions like __add__, __init__, __sub__, etc. are called Dunder Functions

# In the code below, we're making a class that adds and subtracts two complex numbers
# using dunder functions

class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showComplex(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(4, 6)
num1.showComplex()

num2 = Complex(4, 4)
num2.showComplex()

ans = num1 - num2
print("---------")
ans.showComplex()
