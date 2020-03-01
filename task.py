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


def firstAndLast(theList):
    size = len(theList)
    if size < 1:
        return []
    elif size == 1:
        first = theList[0]
        return [first, first]
    else:
        first = theList[0]
        last = theList[size-1]
        return [first, last]
