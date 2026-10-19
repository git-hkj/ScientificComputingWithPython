# An object attributes belongs to a particular object, a class attribute is a variable that belongs to a class but not a particular object. 
# It's shared among all objects of the class
# Class attributes are usually defined outside the __init__() constructor
print("--------------------------------------------------")
class Polynomial():
    '''
    A class of polynomials
    '''
    count = 0

    # class constructor
    def __init__ (self, coefficient):
            '''
            Initialize coefficient attributes of a polynomial
            '''
            self.coeff = coefficient
            #Class Attribute
            Polynomial.count += 1
    def degree(self):
        '''
        Computing the degree of a polynomial
        '''
        return len(self.coeff)-1
    def __del__(self):
        '''
        Deletes the polynomial object
        '''
        Polynomial.count -=1
print("Number of polynomial objects initially :", Polynomial.count)
poly01 = Polynomial([1])
poly02 = Polynomial([2,4])
poly03 = Polynomial([3,5,7])
print("Number of polynomial objects after creation:", Polynomial.count)
del poly03
print("Number of polynomial objects after a deletion:", Polynomial.count)

class Scalar():
    count = 0

    # class constructor
    def __init__ (self):
            self.coeff = [1]    #object attribute self.coeff has default value 1
            #Class Attribute
            Scalar.count += 1
    def __del__(self):
        '''
        Deletes the polynomial object
        '''
        Scalar.count -=1

poly04 = Scalar()
print("Polynomial 04 coefficient :", poly04.coeff)   #poly04.coeff is an object coefficient
poly04.coeff = [2,2]
print("Polynomial 04 coefficient after update:", poly04.coeff)
print("Scalar count before reset :", Scalar.count)
Scalar.count = 0
print("Scalar count after reset :", Scalar.count)


# Assignment
print("-------------------------Assignment-------------------------")
class Rectangle():
    count = 0
    totalArea = 0
    def __init__(self, length, width):
        self.length = length
        self.width  = width        
        Rectangle.count += 1
    def area(self):
        Rectangle.totalArea += self.length * self.width
        return self.length * self.width
    def perimeter(self):
        return 2.0*(self.length + self.width)
    def __del__(self):
            Rectangle.count -=1
rectangleList = []
while False:
    print("Enter the dimension of a rectangle")
    length  = float(input("\t Length :"))
    breadth = float(input("\t Breadth:"))
    if length <= 0.0 or breadth <= 0.0:
        print("Invalid Entries")
        break
    else:
        rectangleList.append(Rectangle(length,breadth))
        print("Area of the rectangle is      :", rectangleList[-1].area())
        print("Perimeter of the rectangle is :", rectangleList[-1].perimeter(),"\n")
print("Total number of rectangles created :", Rectangle.count)
print("Total area of all rectangles :", Rectangle.totalArea)
print("-------------------------End of Assignment-------------------------")
