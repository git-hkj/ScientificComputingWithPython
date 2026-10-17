# For loops are used to perform sequential traversal
print("--------------------------------------------------")
names = ['Amy', 'Bruce', 'Charles', 'David', 'Eve', 
         'Frank', 'Gary', 'Harry', 'Ian', 'John']
for name in names:
    print(name)
'''
The general structure of a for loop

for item in listOfItems:
    action 1
    action 2
'''

# using for loop to build a list of cubes of first 10 natural numbers
cubes = []
for i in range(1,11):   #range(1,11) means [1,11)
    cube = i**3
    cubes.append(cube)
print("\nThe cube list of first 10 natural numbers :", cubes)

# using for loop for summing first 100 natural numbers
totalSum = 0.0
for i in range(1,101):
    totalSum += i
print("The total sum of 100 natural numbers :", totalSum)

# Nested for loops
A = [[0,0,0],[0,0,0],[0,0,0]] # 3x3 matrix using nested lists
for i in range(0,3):
    for j in range(0,3):
        A[i][j] = (i+1)*(j+1)
print("The updated the matrix :", A)

'''
Looping through a dictionary
    + key-value pairs with the method items()
    + by keys with the method keys()
    + by values with the method values()
'''
methods = {'root':'Newton', 'interpolation':'Lagrange', 'integration':'Simpson'}
# with the method items()
for prob,method in methods.items():
    print("Key :", prob, "Value :", method)
# with the method keys()
for prob in methods.keys():
    print("\tKey :", prob)
# with the method values()
for method in methods.values():
    print(" \t\tValue :", method)

# Assignment
print("-------------------------Assignment-------------------------")
number = int(input("Enter any natural number :"))
factorial = 1
for i in range(1,number+1):
    factorial *= i
print("Factorial of the number is :", factorial)
print("-------------------------End of Assignment-------------------------")