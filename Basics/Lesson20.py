# OOP breaks the programming the task into objects, which combine data member(attributes) and functions (members) 
# dot notation is to call any method in the class to act on the object
print("--------------------------------------------------")
class Polynomial():
    '''
    A class of polynomials
    '''
    count = 0
    # class constructor
    def __init__ (self,coefficient):
        '''
        Initialize coefficient attributes of a polynomial
        '''
        Polynomial.count += 0
        self.coeff = coefficient
    def degree(self):
        '''
        Computing the degree of a polynomial
        '''
        return len(self.coeff)-1
    def Evaluate(self,x):
        '''
        Evaluate the polynomial
        '''
        n = self.degree()
        sum =0
        for i in range(0,n+1):
            sum += self.coeff[i]*x**i
        return sum
    def EvaluateList(self, x):
        '''
        Evaluate the polynomial
        '''
        n = self.degree()
        p = []

        for k in x:
            sum = 0
            for i in range(0,n+1):
                sum += self.coeff[i]*k**i
            p.append(sum)
        return p
    def __del__(self):
        '''
        Deletes the polynomial object
        '''
        Polynomial.count -=1

polynomial01 = Polynomial([1,2,3])                                  # 1 + 2*x +3*x**2
print("Coefficient of the polynomial :",polynomial01.coeff)         #polynomial.coeff is an object attribute
print("Degree of Polynomial :",polynomial01.degree())               #polynomial.degree() invokes the method
evlX = float(input("Enter any number to evaluate the polynomial :"))
sol = polynomial01.Evaluate(evlX)
print("Solution of the polynomial is :", sol)
polynomial02= Polynomial([1,6,15,20,15,6,1])                        #(1+x)**6
print("Coefficient of the polynomial (1+x)^6]:",polynomial02.coeff)         #polynomial.coeff is an object attribute
print("Degree of Polynomial (1+x)^6]:",polynomial02.degree())               #polynomial.degree() invokes the method
solList = polynomial02.EvaluateList([-2,-1,0,1,2])
print("Solutions of the polynomial is (1+x)^6]:", solList)

# Assignment
print("-------------------------Assignment-------------------------")

print("-------------------------End of Assignment-------------------------")
