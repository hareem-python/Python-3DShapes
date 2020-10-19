import random
import sys
import os

#define classes and functions for 3 different 3D shapes
class Circle():
    def __init__(self, radius=1):
        self.__radius = radius
        self.display()

    def find_area(self):
        a = self.__radius * self.__radius * 3.142
        return(a)

    def setRadius(self, rad):
        self.__radius = rad

    def getRadius(self):
        return(self.__radius)

    def display(self):
        return(self.find_area())

class Square():
    def __init__(self, sside=2.3):
        self.__sside = sside
        self.display()

    def find_area(self):
        a = self.__sside * self.__sside 
        return(a)

    def setSSide(self, lw):
        self.__sside = lw

    def getSSide(self):
        return(self.__sside)

    def display(self):
        return(self.find_area())

class Cube():
    def __init__(self, cside=2):
        self.__cside = cside
        self.display()

    def find_surfacearea(self):
        sa = 6 * self.__cside * self.__cside
        return(sa)

    def setCSide(self, lwh):
        self.__cside = lwh

    def getCSide(self):
        return(self.__cside)

    def display(self):
        return(self.find_surfacearea())


#create lists and append data

myList = []

circle = 1
square = 2
cube = 3

circlecount = 0
squarecount = 0
cubecount = 0

for i in range (10):
    shape = random.randint(1, 3)
    
    if shape == 1:
        circlecount += 1
        myList.append(1)
        
    elif shape == 2:
        squarecount += 1
        myList.append(2)

    else:
        cubecount += 1
        myList.append(3)
        
print("Circle")
print(circlecount)
print(" ")
print("Square")
print(squarecount)
print(" ")
print("Cube")
print(cubecount)
print(" ")
print(myList, "| Total:", len(myList))

#create and run loops to return properties of shapes
#ask for user input to save output to file, ask for file name if yes
choice = input("\nWould you like to save the output to a file?  Y/N ")
print("")

if choice.lower() == "n" or choice.lower() == "no":
    for i in range(10):

        if myList[i] == 1:
            radius = random.randint(1, 20)
            circle = Circle(radius)
            print("")
            print("Class = Circle")
            print("The area of circle is ",circle.display())
            

        elif myList[i] == 2:
            sside = random.randint(1, 20)
            square = Square(sside)
            print("")
            print("Class = Square")
            print("The area of square is ",square.display())
            

        else:
            cside = random.randint(1, 20)
            cube = Cube(cside)
            print("")
            print("Class = Cube")
            print("The area of cube is ",cube.display())
            

elif choice.lower() == "y" or choice.lower() == "yes":

    filename = input("Enter a filename: ").strip()
    fo = open(filename, "w")

    for i in range(len(myList)):

        if myList[i] == 1:
            radius = random.randint(1, 20)
            circle = Circle(radius)
            fo.write ("\nClass = Circle\nThe area of circle is "+str(circle.display())+"\n")

        elif myList[i] == 2:
            sside = random.randint(1, 20)
            square = Square(sside)
            fo.write ("\nClass = Square\nThe area of square is "+str(square.display())+"\n")

        else:
            cside = random.randint(1, 20)
            cube = Cube(cside)
            fo.write ("\nClass = Cube\nThe area of cube is "+str(cube.display())+"\n")

    fo.close()

else :
    print ("Invalid input.")


