import os
os.system('cls')
import modulestuff

#Outside of built in functions, like print(), you can create your own functions

#this is the function
def namer(name):
    print("Hello %s" % name)

#this is the call. 
namer("bob")
namer("Nate")

#Same code is ran each time with a different value passed in and the print  run on it
#values can also be returned

def adder(x,y):
    z = x+y
    return z

a = adder(2,3)
print(a)

#Functions can also be called from another file if they are imported
print(modulestuff.hello("Nate"))