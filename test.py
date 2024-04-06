import sympy
import math
import numpy as numpy

def OIU(n):
    I=[0,0]
    S=""
    for i in range(0,n+1):
        S= S +"(%i,%i)U" %(i,i+1)
    return S

print(OIU(4))