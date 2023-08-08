import os
os.system('cls')

#conditinal statements are built off comparisions
#first true stament runs
num = 3

if num < 10:
    print("less than 10")
elif num == 10:
    print("equals 10")
else:
    print("greater than 10")

#conditionals are blocks and tabbed 
#conditionals can also require multiple trues or different trues

if num > 10 and num < 100:
    print("greater than 10 and less than 100")
else:
    print("failed one condition")

if num > 10 or num < 100:
    print("one condition is true")

#conditions can also be used for looping.
#note loops will run until they are no longer true. beware the infinite loop
#loop with while on a conditional check
#requires incrementation
x=1
while x < 10:
    print(x)
    x+=1
#itterate through a known list, tuple, or dictionary
z=[1,2,3,4,5,6,7,8,9, 10]
for i in z:
    print(i)

#can also end earlier with a conditional
for i in z:
    print(i)
    if i == 5:
        break