# A function is a set of statement that takes some inputs, do some specific computation and produce output.
# The idea is to put the some commonly/repeatedly done task together and make a function so that instead of 
# writing the same code again and again for different inputs, we call the function 
# def keyword is used to declare user defined functions, 
# an indented block of statements follows the function name and arguments which contains the body of the function
'''
def functionName():
    statements
    .
    .
    .
    return values
'''
print("--------------------------------------------------")
# write a function to find roots of a quadratic equation
'''
 ax^2 + bx + c = 0
 x = (-b +- sqrt(b^2-4ac))/2a, a != 0
'''
def SolveQuadratic(a, b, c):
    """
    Finding the roots of a quadratic equation ax^2 + bx + c = 0

    Input: coefficients a, b, and c
    Output: two real roots x1, x2
    Algorithm: Quadratic Formula
    """
    discriminant =  b**2 - 4.0*a*c
    if(a == 0):
        print("Not a quadratic equation")
        return 0
    else:
        x1 = (-b + discriminant**0.5)/(2.0*a)
        x2 = (-b - discriminant**0.5)/(2.0*a)
        return x1, x2

# calling the function
# a=5, b=5, c=1
root1, root2 = SolveQuadratic(5,6,1)
print("Roots are ",root1, "and", root2)

if __name__ == "__main__":
    print(SolveQuadratic.__doc__)

# Assignment
print("-------------------------Assignment-------------------------")
def CalculateAreaOfCircle(r):
    """
    Calculated area of a circle by using its radius
    Input: radius of the circle
    Output: area of the circle
    Algorithm: Area of circle formula A = pi*r*r
    """
    pi = 3.141592653589793
    return pi*r*r
radius = 1
while radius > 0:
    # taking radius as input
    radius =  float(input("Enter radius of a circle :"))
    if radius <= 0:
        print("Invalid radius")
        break
    else:
        # calling the function
            area = CalculateAreaOfCircle(radius)
            print("Area of the circle :", area)
print(CalculateAreaOfCircle.__doc__)
print("-------------------------End of Assignment-------------------------")
