import os
os.system('cls')

#basic math
#variables can be used or it can even be done directly in a statement like print
a = 1
b = 2
print(a+b)
print(b*4)
print(6/b)
print(b-a)
print(10**b)
print(7%b)

#Order of operations matters
print(3 + 1 * 4)
print((3+1)*4)

#Whole numbers are integers
#Floats are decimals

integer1 = 10
integer2 = 3
print(integer1/integer2)
print(int(integer1/integer2))
print(round((integer1/integer2), 4))

#Numbers will default to what they are unless overridden

num = 100
num2 = 100.11
print(int(num2))
print(float(num))

#math on a varible by itself does not chenge it
print(num)
print(num+5)
print(num)

#update and assign at the same time
print(num)
num += 5
print(num)


