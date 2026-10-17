# if statements allow us to examiune conditions(logical statements) fo decision making
# Logical statement involve the use of relational/comparision operators (==, !=, <, >, >=, <=)
print("--------------------------------------------------")
principal = [12000, 40000, 2000, 18000, 1500, 600, 90000]

if principal:   # python returns TRUE if a list contains at least one item
    print("Calculating interests on accounts")
else:   # empty list
    print("No accounts")

amount = []
for balance in principal:
    if balance > 10000:
        amount.append(int(balance * 1.1))
    else:
        amount.append(int(balance * 1.02))
print("Update balance in the accounts :", amount)


# Assignment
print("-------------------------Assignment-------------------------")
number = float(input("Enter any integer: "))
if(number > 0.0):
    print("Positive number entered")
elif(number < 0.0):
    print("Negative number entered")
else:
    print("Zero entered")
print("-------------------------End of Assignment-------------------------")
