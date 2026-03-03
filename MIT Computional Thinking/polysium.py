import math


def polysum(n,s):
    pi = math.pi
    area = (.25 *n*(s**2))/(math.tan(pi/n))
    boundary = n * s
    area_poundary = area + boundary**2
    area_format = "%.4f" % area_poundary
    print(area_format)
    
polysum(25,99)