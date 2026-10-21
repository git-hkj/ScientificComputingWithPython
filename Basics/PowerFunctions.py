def square(num):
    '''
    Returns the square of the number
    '''
    return num**2

def cube(num):
    '''
    Returns the cube of the number
    '''
    return num**3

def quadroots(a,b,c=-9):
    '''
    Finding roots of the quadratic equation ax^2 + bx + c = 0
    Input: coefficient a,b,c
    Output: two real roots x1,x2
    Algorithm: Quadratic formula
    '''
    discriminant = b**2 - 4*a*c
    x1 = (-b + discriminant**0.5)/(2*a)
    x2 = (-b - discriminant**0.5)/(2*a)

    return x1,x2