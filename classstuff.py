import os
os.system('cls')

#A class is the framework for objects. Example a house is a house, but not all houses are the same the class would be house the values would describe the house. A class can also contain other classes. for example a door may be a class of a house class. there are many types of doors but a door is still a door and the door object is the description of the door built from the door class.

class Square:
    def __init__(self, side:int) -> None:
        self.side = side

    def area(self):
        return self.side **2
    
    def perimiter(self):
        return self.side*4
    

mysquare = Square(8)
print(mysquare.side)
print(mysquare.area())
print(mysquare.perimiter())