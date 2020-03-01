import math


def firstrun():
    return "success"

def circleArea(radius):
    if radius < 0:
        return None
    elif radius == 0:
        return 0
    else:
        Area = math.pi*radius*radius
        return Area
