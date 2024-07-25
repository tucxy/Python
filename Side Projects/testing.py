import math
from sympy import solve, symbols

x = symbols('x')

print(solve(x**3 - 32*x**2 +23*x -2,x))
