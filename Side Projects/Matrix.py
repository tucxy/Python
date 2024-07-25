from sympy import Matrix, symbols, I, simplify, solve

#Function that returns a list of variables designed for sympy base on 'name' and 'size'
def defvar(number,name):
    varlist=[]
    for i in range(1,number+1):
        varlist.append(symbols("%s"%(name)+"%i"%(i)))
    return varlist

def defmultvar(*names):
    varlist=[]
    var=""
    for s in names:
        var = symbols("%s"%(s))
        varlist.append(var)
    return varlist

x= symbols("x")
y = symbols("y")

B = Matrix([[1,3],
[2,7]])

Binv = B.inv()
D = Matrix([[10000],
[20000]])

A = Matrix([[-4,2],
[0,3]])


print(B.inv())