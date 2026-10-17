# while loop runs as long as a certain condition is TRUE
print("--------------------------------------------------")
x = 1

while x**3 <= 9999:
    x += 1
    print("x = ",x," and its cube = ", x**3)
print("Cube exceed 10000")
x -=1
print("The last number is ",x, "and it cube ",x**3)

# Assignment
print("-------------------------Assignment-------------------------")
number = 1
threshold = 67
while number != threshold:
    number = int(input("Enter any number between 1 and 100 :"))
print("Guess correct ", threshold)
print("-------------------------End of Assignment-------------------------")
