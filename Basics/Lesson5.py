# Swapping two values 

print("\n")
first = float(input("Enter the first value: "))
second = float(input("Enter the second value: "))

first = first + second
second = first - second
first = first - second

print("After swapping:")
print("First value:", first)
print("Second value:", second)
