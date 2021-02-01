# This script calculates an angle or a side using law of cosines
import math


def validFloatInput():
    try:
        inputFloat = float(input("> "))
        return inputFloat
    except ValueError:
        print("Enter a valid number")
        validFloatInput()


def calculateSide():
    print("Enter a number for side a")
    sideA = validFloatInput()

    print("Enter a valid number for side b")
    sideB = validFloatInput()

    print("Enter a number for angle C in degrees")
    angleC = validFloatInput()

    sideC = math.pow(sideA, 2) + math.pow(sideB, 2) - 2 * sideA * sideB * math.cos(math.radians(angleC))
    print("Side C Squared = " + str(sideC))

    sideC = math.sqrt(sideC)
    print("Side C = " + str(sideC))


def calculateAngle():
    print("Enter a number for side a")
    sideA = validFloatInput()

    print("Enter a number for side b")
    sideB = validFloatInput()

    print("Enter a number for side c")
    sideC = validFloatInput()

    sideC = math.pow(sideC, 2)
    d = math.pow(sideA, 2) + math.pow(sideB, 2)
    e = -2 * sideA * sideB
    sideC -= d
    e = sideC / e

    if e < 0:
        alpha = math.degrees(math.acos(abs(e)))
        print("Alpha = " + str(alpha))
        angleC = 180 - alpha
        print("Angle C = " + str(angleC))
    else:
        angleC = math.degrees(math.acos(abs(e)))
        print("Alpha = " + str(angleC))
        print("Angle C = " + str(angleC))


print("Law of Cosines")
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
