# This script calculates an angle or a side using law of sines
import AngleConversions
import math


def calculateSide():
    validFloat = False
    while not validFloat:
        angleA = input("Enter a number for angle A in degrees\n")
        if angleA.isnumeric():
            angleA = float(angleA)
            validFloat = True
        else:
            print("Input a valid real number")

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
        angleB = input("Enter a number for angle B in degrees\n")
        if angleB.isnumeric():
            angleB = float(angleB)
            validFloat = True
        else:
            print("Input a valid real number")

    sideB = (sideA * math.sin(AngleConversions.convertRadians(angleB))) / math.sin(
        AngleConversions.convertRadians(angleA))

    print("Side B = " + str(sideB))


def calculateAngle():
    validFloat = False
    while not validFloat:
        angleA = input("Enter a number for angle A in degrees\n")
        if angleA.isnumeric():
            angleA = float(angleA)
            validFloat = True
        else:
            print("Input a valid real number")

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

    sinB = (sideB * math.sin(AngleConversions.convertRadians(angleA))) / sideA
    if sinB > 1 or sinB < 0:
        print("There are no possible angles that will work in this triangle.")
    else:
        angleB = AngleConversions.convertDegrees(math.asin(sinB))
        angleB2 = 180 - angleB
        print("Angle B =\n" + str(angleB) + "\n" + str(angleB2))


print("Law of Sines")
validInt = False
while not validInt:
    decision = input("Press 1 to calculate a side\nPress 2 to calculate an angle\n")
    if decision.isnumeric() and (decision == '1' or decision == '2'):
        validInt = True
        decision = int(decision)
        if decision == 1:
            calculateSide()
        elif decision == 2:
            calculateAngle()
    else:
        print("Please Enter 1 or 2")
