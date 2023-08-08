import os
os.system('cls')

#Data Types
#Strings
#A string is just a group of characters in quotes
aString = "This is an example of a string. It can be basically anthing you need it to be. Using a number like 452 does not act like a number, and you cannot do math on it like that."
print(aString)

#Numbers
#Numbers com in two types. Integers are whole numbers and Floats are numbers with a decimal
aNumberInt = 452
aNumberFloat = 452.989
print(aNumberInt)
print(aNumberFloat)

#Lists aka array
#A list is a group of strings or numbers collected together in a bucket. The list is indexed starting at zero. Lists are mutable
aList = ["This is the first but is index 0", "A list can be a long string", "or", 452, "whatever you need"]
print(aList)
print(aList[0])

#Tupples
#just like a list only what you have you are stuck with because they are immutable
aTupple = ("Looks like a list", 452, "but you are stuck with what you have and cannot edit it")
print(aTupple[1])

#Dictionaries
#A list like set up with key:value pairs matching the "key" to the "value"
aDictionary= {
    "firstKey": "First Key Value",
    "newKey": "Convention is to stack them",
    "lastKey": "It makes it easier to read"
}
print(aDictionary["firstKey"])
