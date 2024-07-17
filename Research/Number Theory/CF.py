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


x = Decimal(1.4142135623730950488016887242096980785696718753769480731766797379)
r = Decimal(3) / Decimal(2)
n = 100

result = fincf(x, r, n)[1]
print(result)
