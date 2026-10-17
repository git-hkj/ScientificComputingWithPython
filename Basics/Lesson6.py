# Lists are used to store multiple items in a single variable
x = 3.0
mixedList = ['item0', 1, x, '3', [1, 2, 3], True, 10.354]
print("--------------------------------------------------")
print("Type of mixed_list:", type(mixedList))
print("Mixed list contains:", mixedList)

#Accessing items from a list
first_item = mixedList[0]
print("Length of the list is:", len(mixedList))
last_item = mixedList[-1]
print("Last item in the list is:", last_item)

#Slicing a list -> lower index is inclusive, upper index is exclusive
print("Sliced list [1:4]:", mixedList[1:4])  # slicing 1:4 means [1,4)
print("Sliced list [1:]:", mixedList[1:])   # slicing 1: means [1,end)

#Performing operations on a list
print("First item in the list is:" + first_item)
x /= mixedList[-1] - 0.354
print("Value of x after operation:", x)
fibonacciList = list([1,1,2,3,5,8,13,21])
print("Fibonacci sequence:", fibonacciList)

#Range creates a list using a start, end and step size; only the start is inclusive
print("New integer list:", list(range(-10, 11)))    
print("New integer list in decresing order:", list(range(10, -11, -1)))    

#Inserting an element at a particular index
mixedList.insert(2,False)
print("The updated mixed list:", mixedList)

#Removing an element from the list, it removes only the first occurence of the element
fibonacciList.remove(1)
print("Updated Fibonacci sequence:", fibonacciList)

#Immutable list -> Tuple; it doesn't support item assignment
spatialDimensions = ('x','y','z')
print("Tuple for spatial dimensions:", spatialDimensions)
print("Size of the spatial dimensions tuple:", len(spatialDimensions))

# Assignment
print("-------------------------Assignment-------------------------")
numberList = list(map(int, input("Enter numbers separated by spaces: ").split()))
evenSum = 0
for number in numberList:
    if number % 2 == 0:
        evenSum += number
print("Sum of even numbers:", evenSum)
print("-------------------------End of Assignment-------------------------")
