# continue statement in a loop skip the remaining code in the loop body and returns to 
# the beginning of the loop with the next value of the loop variable
print("--------------------------------------------------")
x = 0
while x <=30:
   x += 1
   if x%2 == 0:
      continue
   print(x, "is a odd number")

for x in range(1,31):
    x += 1
    if x%2 == 0:
          continue
    print(x, "is a odd number")
    
# Assignment
print("-------------------------Assignment-------------------------")
skip = 10
for i in range(1,21):
    if i== skip:
        print("Skipped")
        continue
    else:
        print("Number :", i)
print("-------------------------End of Assignment-------------------------")
