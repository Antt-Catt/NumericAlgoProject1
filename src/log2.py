from decimal_ import *

def calc_log(p):
    res = 0
    for n in range(1, 1000000):
        if n % 2 == 0:
            res -= 1/n
        else:
            res += 1/n
    return rp(res,p)

print(calc_log(20))
