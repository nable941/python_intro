import os
os.system('cls')

#Strings can use "" or '' but have to be paired together with the same
#Use on or the other to display the other in a string
#or use an escape character like \

showDoubleQuote = 'this is in single quotes to show "double quotes" in the string'
showSingleQuote = "this is in double quotes to show 'single quotes' in the string"
doubleWithEscape = "this is \"Double quoted\" using escape "

print(showSingleQuote)
print(showDoubleQuote)
print(doubleWithEscape)

#use \n as a carraige return to the next line
twoLines = "this string is\non two lines"
print(twoLines)

#Strings can be manipulated. They are mutable
myString = "my name is Nathan Able"
print(myString)
#uppercase
print(myString.upper())
#lowercase
print(myString.lower())
#capitolize
print(myString.capitalize())
#title
print(myString.title())
#swapcase
print(myString.swapcase())

#get the length of the string (character count)
print(len(myString))

#get specific characters
print(myString[1])
print(myString[11:len(myString)])

#break string into a list
print(myString.split(' '))