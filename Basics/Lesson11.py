# break statement in for or while loop terminates the loop without any remaining code in the loop body
print("--------------------------------------------------")
num = 1729
temp = 0
for i in range(2,num):
    if num%i == 0:
        print(num," = ", i, "x", num//i)
        break
    temp = i
if temp == num-1:
    print(num, "is a prime number")

prompt = "\n Enter a positive number to check if it's prime"
prompt += "\n (Enter -1 when you are done) :"
while True:
    num =int(input(prompt))
    if num == -1:
        break
    else:
        temp = 0
        for i in range(2,num):
            if num%i == 0:
                print("\t",num," = ", i, "x", num//i)
                break
            temp = i
        if temp == num-1:
            print("\t",num, "is a prime number")


# Assignment
print("-------------------------Assignment-------------------------")
totalSum = 0
number = 1
while True:
    number = int(input("Enter any number :"))
    totalSum += number
    if number ==0:
        break
print("The sum of all the numbers entered so far :", totalSum)
print("-------------------------End of Assignment-------------------------")
