# This script calculates the area of a triangle using two sides and an angle
import math


def validFloatInput():
    try:
        inputFloat = float(input("> "))
        return inputFloat
    except ValueError:
        print("Enter a valid number")
        validFloatInput()


print("Enter a number for side a")
sideA = validFloatInput()

print("Enter a number for side b")
sideB = validFloatInput()

print("Enter a number for angle C in degrees")
angleC = validFloatInput()

area = 0.5 * sideA * sideB * math.sin(math.radians(angleC))
print("The area of a triangle is " + str(area))
