import math
import AngleConversions


def calculateSide():
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
        sideB = input("Enter a number side b\n")
        if sideB.isnumeric():
            sideB = float(sideB)
            validFloat = True
        else:
            print("Input a valid real number")

    validFloat = False
    while not validFloat:
        angleC = input("Enter a number for angle C in degrees\n")
        if angleC.isnumeric():
            angleC = float(angleC)
            validFloat = True
        else:
            print("Input a valid real number")

    sideC = \
        math.pow(sideA, 2) + math.pow(sideB, 2) - 2 * sideA * sideB * math.cos(AngleConversions.convertRadians(angleC))

    print("Side C Squared = " + str(sideC))
    sideC = math.sqrt(sideC)
    print("Side C = " + str(sideC))


print("Law of Cosines")
validInt = False
while not validInt:
    decision = input("Press 1 to calculate a side\nPress 2 to calculate an angle\n")
    if decision.isnumeric() and (decision == '1' or decision == '2'):
        validInt = True
        decision = int(decision)
        if decision == 1:
            calculateSide()
        #elif decision == 2:
            #calculateAngle()
    else:
        print("Please Enter 1 or 2")
