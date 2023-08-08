import os
os.system('cls')

myList = ["book", "pizza", "candy"]
numList = [1,2,3,4,5]
mixList = ["chair", 42, 5.7]

#Access a list by it's index starting at 0
print(myList[0])
print(numList[1])
print(mixList[2])

#list can contain lists
nestedList = ["car", "tree", myList]
print(nestedList)
print(nestedList[2])
print(nestedList[2][1])

#lists can be edited
#Change Valuse
print(myList)
myList[2] = "car"
print(myList)
#add value
myList.append("candy")
print(myList)
#delete value
del myList[0]
print(myList)

#Tupples are like lists except the editing will not work and it is surrounded by () instead of []
