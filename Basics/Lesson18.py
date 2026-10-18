# Class can be regarded as a template for creating real world objects 
# A class tells us what data an object should have, what are the initial/default values of the data, 
# and what methods are associated with the object to take actions on the objects using their data
# An object is an instance of a class, and creating an object from a class is called instantiation.
print("--------------------------------------------------")
class Polynomial():
    '''
    A class of polynomials
    '''
    # class constructor
    def __init__ (self,coefficient):
        '''
        Initialize coefficient attributes of a polynomial
        '''
        self.coeff = coefficient
    def degree(self):
        '''
        Computing the degree of a polynomial
        '''
        return len(self.coeff)-1

polynomial01 = Polynomial([1,2,3])
print(polynomial01.coeff)       #polynomial.coeff is an object attribute
print(polynomial01.degree())    #polynomial.degree() invokes the method


# Assignment
print("-------------------------Assignment-------------------------")
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width        
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2.0*(self.length + self.width)
while True:
    print("Enter the dimension of a rectangle")
    length  = float(input("\t Length :"))
    breadth = float(input("\t Breadth:"))
    if length <= 0.0 or breadth <= 0.0:
        print("Invalid Entries")
        break
    else:
        userRectangle = Rectangle(length,breadth)
        print("Area of the rectangle is      :", userRectangle.area())
        print("Perimeter of the rectangle is :", userRectangle.perimeter(),"\n")
print("-------------------------End of Assignment-------------------------")
