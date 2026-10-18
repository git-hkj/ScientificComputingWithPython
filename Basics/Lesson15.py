# Functions can contains two types of arguments : positional and keyword 
# positional arguments needs to be included in the proper position or order
# keyword arguments are passed to a function which is preceded by a keyword and an equals sign  
# the form is: function(keyword = value)
# keyword argument are key-value pairs passed to a function
# a key-value pair associates the parameter name of the function with the argument value of the function call 
# key-value pairs in a function call clairfy the role of each value and free us from worrying about the correct order of arguments
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

a1 = 5
b1 = 6
c1 = 1
# calling the function with keyword arguments
x1,x2 = SolveQuadratic(c=c1, b=b1, a=a1)
print("Roots are ",x1, "and", x2)



# Assignment
print("-------------------------Assignment-------------------------")
def CalculateBoxVolume(l,b,h):
    """
    Calculates volume of a box using its dimensions
    Input: all three dimensions of the box(length, breadth, height)
    Output: volume of the box
    Algorithm: Volume of the box formula V = length * breadth * height
    """
    return l*b*h
       
while True:
    print("Enter the dimensions of the box")
    l = float(input("\tLength   :"))
    b = float(input("\tBreadth  :"))
    h = float(input("\tHeight   :"))
    if l<=0 or b<=0 or h <=0:
            print("Invalid entry")
            break
    else:
        volume = CalculateBoxVolume(l,b,h)
        print("Volume of the box is :", volume,"\n")
print(CalculateBoxVolume.__doc__)
print("-------------------------End of Assignment-------------------------")
