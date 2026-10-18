# Immutable object cannot be changed after it is created. These are built-in type like int, float, string, tuple, bool
# Mutable object can change their state or contents, they are of type list, dict, set
# Pass-by-value     : immutable object passed to a function by copying its value to the corresponding parameter in the function. Any change done to the parameter will not change the original variable
# Pass-by-reference : when a mutable object is passed to a function, the function can gain direct access to it. Therefore, changes made to the object inside the function will be visible outside as well
#
#
print("--------------------------------------------------")
def PassByValue(x):
    x = 5
    print("Inside the function x value now :",x)

x = 1
print("Initial x value :", x)
PassByValue(x)
print("Current value of x after function :", x)

def PassByReference(listReceived):
    listReceived[0] = 1
    listReceived.append(2)

listSent= [0]
print("The initial list :", listSent)
PassByReference(listSent)
print("The list after function call :", listSent)

# Assignment
print("-------------------------Assignment-------------------------")
def AdaptList(num, listReceived):
    for i in range(len(listReceived)):
        num += i
        listReceived[i]=num
    print("Number during the function :", num)
num = int(input("Enter any natural number:"))
newList = list(map(int, input("Enter numbers separated by spaces: ").split()))
AdaptList(num, newList)
print("The number after function call :", num)
print("The list after function call :", newList)
print("-------------------------End of Assignment-------------------------")
