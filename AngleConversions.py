import math


def convertRadians(angle):
    angle = float(angle)
    return (angle * math.pi) / 180


def convertDegrees(angle):
    angle = float(angle)
    return (angle * 180) / math.pi
