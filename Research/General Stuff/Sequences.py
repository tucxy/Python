import math

def classes(n):

    sevenmod14 = []
    eightmod14 = []
    for i in range(0,n):
        x = 14*i+7
        y = 14*i+8
        sevenmod14.append(x)
        eightmod14.append(y)

    return sevenmod14,eightmod14

n = 99

seven = classes(n)[0]
eight = classes(n)[1]

def div(H,m):
    new = []
    for i in H:
        s = i
        if s % m == 0:
            new.append(f"{s}*")
        else:
            new.append(i)
    return new
            

print(seven)
print("\n")
print(eight)
print("\n")
print(div(seven,3))
print("\n")
print(div(eight,3))
