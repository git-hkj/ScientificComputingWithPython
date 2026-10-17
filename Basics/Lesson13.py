# a function is named block of code that carries out a specific task.
# a method is a function associated with an object(e.g. list, dictionary, tuple, string, set, etc) and operates on the object.
# in order to get all builtin functions of python, execute this in python command line -> dir(__builtin__)
print("--------------------------------------------------")
prompt = "\n Enter a number :"
num =  input(prompt)
print(num, "is of the type", type(num))
try:
    num = int(num)  # explicit type conversion
    print(num, "is now of the type", type(num))
except ValueError:
    try:
        num = float(num)
        print(num, "is now of the type", type(num))
    except ValueError:
        print("Oops, cannot convert ", num, "into numeric representation")
        print("Please enter a number")
#ValueError(Exception) -> Inappropriate argument value (of correct type).
