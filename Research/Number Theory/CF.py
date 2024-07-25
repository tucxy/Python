import math
from decimal import Decimal, getcontext


getcontext().prec = 100

def fincf(x, r, n):
    x = Decimal(x)
    r = Decimal(r)

    X = [x]
    A = [math.floor(x)]
    term = 0

    for i in range(n):
        if X[i] == Decimal(math.floor(X[i])):
            term = i
            break
        else:
            xc = r / (X[i] - Decimal(math.floor(X[i])))
            ac = math.floor(xc)

            X.append(xc)
            A.append(ac)
    
    return X, A, term


x = Decimal(math.sqrt(2))
r = Decimal(3) / Decimal(2)
n = 100

result = fincf(x, r, n)[1]
print(result)
