# Special symbols for passing variable number of arguments: 
# *args -> non keyword arguments, to pass variable number of position arguments 
# it allows to take in more arugments than the number of formal arguments in the function definition
# **kwargs -> keyword  
#  kwargs can be thought as a dictionary that maps each keyword to the value that we pass alongside
print("--------------------------------------------------")
def testFunc01(arg1,*args):
    print(arg1)
    for arg in args:
        print(arg)
testFunc01('Python','for','Scientific','Computing')
testFunc01('Python','for','Scientific','Computing ','Introduction', 'to', 'NumPy')

def testFunc02(arg1, **kwargs):
    for key,value in kwargs.items():
        print(key, " = ", value)
    print(arg1)
testFunc02('Course', first = 'Python', second='for', third='Scientific', fourth='Computing')

def testFunc03(arg1, arg2, arg3, arg4):
    print("First     :", arg1)
    print("Second    :", arg2)
    print("Third     :", arg3)
    print("Fourth    :", arg4)
# *args to pass arguments
args = ('Python', 'for','Scientific', 'Computing')
testFunc03(*args)

# **kwargs to pass arguments
kwargs = {'arg1':'Welcome', 'arg2': 'to', 'arg3':'the', 'arg4':'course'}
testFunc03(**kwargs)

# Assignment
print("-------------------------Assignment-------------------------")
def sumNumbers(*args):
    return sum(args)
numList = list(map(int, input("Enter numbers separated by spaces: ").split()))
sum = sumNumbers(*numList)
print("Sum of those number :", sum)
print("-------------------------End of Assignment-------------------------")
