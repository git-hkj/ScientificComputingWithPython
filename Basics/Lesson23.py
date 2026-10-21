# Modular programming : the process of breaking a large, unwidely programming task into separate, smaller, more manageable subtasks/modules
# Functions and classes in separate files are known as modules 
# Advantgages of modularizing code in large application: 
# simplicity(break big complex problem into simple small part), 
# maintainability(every module can be written, modified and tested individual, hence easier to maintainability), 
# reusability(can resused a lot), scoping(modules have their own namescape)
# we can reuse functions and classes from the same modules in many different main programs, and we can share our modules with others or use others modules
# the separation of modules from main programs make the main programs easy to follow and allows us to focus on high-level logic the main function
print("--------------------------------------------------")
import PowerFunctions               #import entire module
import PowerFunctions as solver     #import entire module and give it an alternative name solver
a1 = 1
b1 = 0
root1, root2 = solver.quadroots(c=-16,a=a1,b=b1)
print("The roots :", root1, " ", root2)

# Assignment
print("-------------------------Assignment-------------------------")
from PowerFunctions import square as sq     #import specific function from a module and give it an alternative name
while True:
    number = int(input("Enter any number :"))
    if number <= 0.0:
        break
    else:
        numSq = sq(number)
        print("Square of the number is :", numSq)
print("-------------------------End of Assignment-------------------------")
