import os
os.system('cls')

#Dictionaries are values attached to a key
favSnack = {
    "Nathan": "Pizza", 
    "Michael":"Gummy Bears", 
    "Timmy":"Banana"}

#Type it out stacked to make reading it easier

#call things by thier key instead of index
print(favSnack["Nathan"])

#They can be edited as well
#delete value and key
print(favSnack)
del favSnack["Nathan"]
print(favSnack)

#change value
favSnack["Michael"]= "Apples"
print(favSnack)

#Add to dictionary
favSnack.update({"Nathan":"Pizza"})
print(favSnack)

#because the dictionary uses keys the group is said to be unordered