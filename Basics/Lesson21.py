# Class inheritance helps in extending class functionalites thereby helps in implementing code resuability 
# Specialized class is the child class and general class is parent class 
# Child class can inherit all the attributes and methods from parent class
# Child class can also define its own special attributes and methods, and also override the methods of parent class
print("--------------------------------------------------")
class Polynomial():
    '''
    Class of polynomials (base class)
    '''
    def __init__(self, coefficient):
        '''
        Initialize the coefficient attributes
        '''
        self.coeff = coefficient
    def degree(self):
        '''
        Computing the degree of a polynomial
        '''
        return len(self.coeff)-1

class Quadratic(Polynomial):
    '''
    Class for quadratric polynomials (inherits from base class)
    '''
    def __init__(self, coefficient, powerIncrease=1):
        '''
        Initialize the coefficient attributes
        '''
        super().__init__(coefficient)
        self.powerIncrease = powerIncrease
    def roots(self):
        c = self.coeff[0]
        b = self.coeff[1]
        a = self.coeff[2]
        if self.powerIncrease == -1:
            a = self.coeff[0]
            c = self.coeff[2]
        discriminant = b**2 - 4*a*c
        root1 = (-b + discriminant**0.5)/(2*a)
        root2 = (-b - discriminant**0.5)/(2*a)
        return root1, root2
    def degree(self):
        return 2

quadPoly01 = Quadratic([2,-3,1],1) # creates 2-3x+x^2=0
print("Roots of the 1st quadratic eqn are :", quadPoly01.roots())

quadPoly02 = Quadratic([2,-3,1],-1) # creates 2x^2+-3x+1=0
print("Roots of the 2nd quadratic eqn are :", quadPoly02.roots())


# Assignment
print("-------------------------Assignment-------------------------")
class Shape():
    count =0
    def __init__ (self):
        Shape.count += 1
    def area(self):
        return 1
    def __del__ (self):
            Shape.count -= 1

class Triangle(Shape):
    def __init__(self,height, base):
        self.h = height
        self.b = base
    def area(self):
        return 0.5*self.h*self.b

class Rectangle(Shape):
    def __init__(self, length, breadth):
            self.l = length
            self.b = breadth
    def area(self):
        return self.l *self.b
    
class Circle(Shape):
    def __init__(self,radius):
            self.r = radius
    pi = 3.141592653589793
    def area(self):
        return self.pi*self.r**2

print("Enter dimensions of a triangle")
tHeight = float(input("\t Height of triangle :"))
tBase = float(input("\t Base of triangle :"))
userTriangle = Triangle(tHeight,tBase)
areaT = userTriangle.area()
print("Area of the triangle :", areaT, "\n")

print("Enter dimensions of a rectangle")
rLength = float(input("\t Length of rectangle :"))
rBreadth = float(input("\t Breadth of rectangle :"))
userReactangle = Rectangle(rLength,rBreadth)
areaR = userReactangle.area()
print("Area of the rectangle :", areaR, "\n")

print("Enter dimensions of a circle")
cRadius = float(input("\t Radius of circle :"))
userCircle = Circle(cRadius)
areaC = userCircle.area()
print("Area of the Circle :", areaC, "\n")
print("-------------------------End of Assignment-------------------------")
