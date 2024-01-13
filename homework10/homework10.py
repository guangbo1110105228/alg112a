import numpy as np
from scipy.optimize import fsolve

def polynomial_equation1(x):
    return x**5 + 1

def polynomial_equation2(x):
    return x**8 + 3*x**2 + 1

# x的5次 + 1 = 0
roots1 = fsolve(polynomial_equation1, 0)
print("ans:", roots1)

# x的8次 + 3(x的2次) + 1 = 0
roots2 = fsolve(polynomial_equation2, 0)
print("ans:", roots2)
