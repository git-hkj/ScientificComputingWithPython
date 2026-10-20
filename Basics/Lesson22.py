# When modeling complex things in the real world, we need to think at high logical level rather than a syntax-focused level, 
# and we may want to break a large class into smaller classes that work together.
print("--------------------------------------------------")
class Monomial():
    '''
    A class of monomial
    '''
    def __init__(self,a=1,n=0):
        self.a = a
        self.n = n
    def property(self):
        if self.a > 0:
            print("Positive coefficient :", self.a)
        if self.a < 0:
            print("Negative coefficient :", self.a)
        if self.a == 0:
            print("Zero coefficient :", self.a)
        if self.n%2 == 0:
            print("Even power :", self.n)
        else:
            print("Odd power :", self.n)

class Polynomial():
    '''
    A class of polynomial
    '''
    def __init__(self, coefficients):
        self.coeff = coefficients
        n =  len(coefficients)-1
        a = coefficients[-1]
        self.leadingTerm =  Monomial(a,n)   # atrribute leading term is a monomial object

class Quadratic(Polynomial):
    '''
    A class of quadratic derived from polynomial
    '''
    def __init__(self, coefficients, powerIncrease):
        super().__init__(coefficients)
        self.powerIncrease = powerIncrease  # c + bx + ax^2 = 0
        self.leadingTerm   = Monomial(coefficients[2],2)
        if powerIncrease == -1:
            self.leadingTerm = Monomial(coefficients[0],2)

mono =  Monomial()
print("Default monomial :", mono.property())

poly = Polynomial([1,2,3,4,5])  # a_0 + a_1x + a_2x^2 + a_3x^3 + a_4x^4
print("Leading term of polynomial :",poly.leadingTerm.property())

quadpoly = Quadratic([1,2,3],1)     # 1 + 2x + 3x^2
print("Leading term of polynomial :",quadpoly.leadingTerm.property())

# Assignment
print("-------------------------Assignment-------------------------")
class Student():
    def __init__(self,name, age, major):
        self.name   = name
        self.age    = age
        self.major  = major

class University():
    def __init__(self,studentList):
        self.studentList = studentList
    def totalNoStudent(self):
        return len(self.studentList)    
    def studentInfo(self):
        n = len(self.studentList)
        for i in range(0,n):
            print(i+1,". ",self.studentList[i].name," Age: ",self.studentList[i].age, " Major: ",self.studentList[i].major)
       
studentList = []
while True:
    print("Enter the student details")
    name    = input("\tName :")
    age     = int(input("\tAge :"))
    major   = input("\tMajor :")
    if age <= 0:
        print("Invalid age entry")
        break
    else:
        studentList.append(Student(name,age,major))

uniABC = University(studentList)
print("Info of all", uniABC.totalNoStudent(),"students at the University ABC")
uniABC.studentInfo()
print("-------------------------End of Assignment-------------------------")
