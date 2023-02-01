import math

A = [math.atan(1), math.atan(0.1), math.atan(0.01), math.atan(0.001), math.atan(0.0001)]

def arctan(x):
    if x < 0:
        return -arctan(-x)
    if x > 1:
        return math.pi/2 - arctan(1/x)
    k = 0
    y = 1
    r = 0
    while k <= 4:
        while x < (y*10**(-k)):
            k += 1
        if k <= 4:
            xp = x - y*10**(-k)
            y += x*10**(-k)
            x = xp
            r += A[k]
    return r + (x/y)

print(arctan(1/2))
print(math.atan(1/2))

def tan(x):
    k = 0
    n = 0
    d = 1
    while k <= 4:
        while x >= A[k]:
            x = x-A[k]
            np = n + d*10**(-k)
            d = d - n*10**(-k)
            n = np
        k = k+1;
    return (n+x*d)/(d-x*n)

print(tan(1))
print(math.tan(1))
