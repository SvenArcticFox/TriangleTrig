# This script calculates the area of a triangle using two sides and an angle
import math


def convertRadians(angle):
    angle = float(angle)
    return (angle * math.pi) / 180


validFloat = False
while not validFloat:
    sideA = input("Enter a number for side a\n")
    if sideA.isnumeric():
        sideA = float(sideA)
        validFloat = True
    else:
        print("Input a valid real number")

validFloat = False
while not validFloat:
    sideB = input("Enter a number for side b\n")
    if sideB.isnumeric():
        sideB = float(sideB)
        validFloat = True
    else:
        print("Input a valid real number")

validFloat = False
while not validFloat:
    angleC = input("Enter a number for angle C\n")
    if angleC.isnumeric():
        angleC = float(angleC)
        validFloat = True
    else:
        print("Input a valid real number")


area = 0.5 * sideA * sideB * math.sin(convertRadians(angleC))
print("The area of a triangle is " + str(area))
