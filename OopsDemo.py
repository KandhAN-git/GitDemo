#classes are user defined blueprint or prototype
#sum, multiply, addition, constant
#method, class variable, instance variable, Constructor etc...
#Objects are classes.

class Calculator:
    num = 100 #Class Variable
    #Default constructor

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("Executing method in class")

    def Summation(self):
        return self.a+self.b+Calculator.num

obj = Calculator(2, 3) # Syntax to create objects in python
obj.getdata()
print(obj.Summation())

obj1 = Calculator(5, 8)
obj1.getdata()
print(obj1.Summation())

# 