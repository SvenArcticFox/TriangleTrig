# This script calculates an angle or a side using law of sines
import math


def validFloatInput():
    try:
        inputFloat = float(input("> "))
        return inputFloat
    except ValueError:
        print("Enter a valid number")
        validFloatInput()


def calculateSide():

    print("Enter a number for angle A in degrees")
    angleA = validFloatInput()

    print("Enter a number for side a")
    sideA = validFloatInput()

    print("Enter a number for angle B in degrees")
    angleB = validFloatInput()

    sideB = (sideA * math.sin(math.radians(angleB))) / math.sin(math.radians(angleA))

    print("Side B = " + str(sideB))


def calculateAngle():

    print("Enter a number for angle A in degrees")
    angleA = validFloatInput()

    print("Enter a number for side a")
    sideA = validFloatInput()

    print("Enter a number for side b")
    sideB = validFloatInput()

    sinB = (sideB * math.sin(math.radians(angleA))) / sideA
    if sinB > 1 or sinB < 0:
        print("There are no possible angles that will work in this triangle.")
    else:
        angleB = math.degrees(math.asin(sinB))
        angleB2 = 180 - angleB
        print("Angle B =\n" + str(angleB) + "\n" + str(angleB2))


print("Law of Sines")
validInt = False
while not validInt:
    decision = input("Press 1 to calculate a side\nPress 2 to calculate an angle\n")
    if decision == '1' or decision == '2':
        validInt = True
        decision = int(decision)
        if decision == 1:
            calculateSide()
        elif decision == 2:
            calculateAngle()
    else:
        print("Please Enter 1 or 2")
