from math import sqrt

def areaOfTriangle(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def distBetweenPoints(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def pointBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    ab = distBetweenPoints(x1, y1, x2, y2)
    bc = distBetweenPoints(x2, y2, x3, y3)
    ac = distBetweenPoints(x1, y1, x3, y3)
    
    if (ac >= ab + bc) or (ab >= bc + ac) or (bc >= ab + ac):
        return 0
    
    pFlag = True
    qFlag = True
    
    A = areaOfTriangle(x1, y1, x2, y2, x3, y3)
    
    A1 = areaOfTriangle(xp, yp, x2, y2, x3, y3)
    A2 = areaOfTriangle(x1, y1, xp, yp, x3, y3)
    A3 = areaOfTriangle(x1, y1, x2, y2, xp, yp)
    
    if A != A1 + A2 + A3:
        pFlag = False
    
    B1 = areaOfTriangle(xq, yq, x2, y2, x3, y3)
    B2 = areaOfTriangle(x1, y1, xq, yq, x3, y3)
    B3 = areaOfTriangle(x1, y1, x2, y2, xq, yq)
    
    if A != B1 + B2 + B3:
        qFlag = False
    
    if pFlag and not qFlag:
        return 1 
    elif not pFlag and qFlag:
        return 2 
    elif pFlag and qFlag:
        return 3 
    else:
        return 4