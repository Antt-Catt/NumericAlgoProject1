import math
from decimal_ import rp

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
    x = x % math.pi
    if x > math.pi/2:
        return -tan(math.pi - x)
    if x > math.pi/4:
        return 1/tan(math.pi/2 - x)
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

print(tan(5))
print(math.tan(5))


# NB : valeur fausse pour p >= 13
def test_arctan():

    #x = 0.5
    x = 0.5
    arct_python = math.atan(x)

    #p = 10
    p = 10
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 0.5, p = 10) : \t PASSED")

    #p = 11
    p = 11
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 0.5, p = 11) : \t PASSED")

    #p = 12
    p = 12
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 0.5, p = 12) : \t PASSED")


    #x = 5
    x = 5
    arct_python = math.atan(x)

    #p = 10
    p = 10
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 5, p = 10) : \t PASSED")

    #p = 11
    p = 11
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 5, p = 11) : \t PASSED")

    #p = 12
    p = 12
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 5, p = 12) : \t PASSED")

    #p = 13
    p = 13
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 5, p = 13) : \t PASSED")

    #p = 14
    p = 14
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = 5, p = 14) : \t PASSED")


    #x = -2
    x = -2
    arct_python = math.atan(x)

    #p = 10
    p = 10
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = -2, p = 10) : \t PASSED")

    #p = 11
    p = 11
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = -2, p = 11) : \t PASSED")

    #p = 12
    p = 12
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = -2, p = 12) : \t PASSED")

    #p = 13
    p = 13
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = -2, p = 13) : \t PASSED")

    #x = -0.5
    x = -0.5
    arct_python = math.atan(x)

    #p = 10
    p = 10
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = -0.5, p = 10) : \t PASSED")

    #p = 11
    p = 11
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = -0.5, p = 11) : \t PASSED")

    #p = 12
    p = 12
    arct_python_rp = rp(arct_python, p)
    arct_approx = rp(arctan(x), p)
    assert(arct_python_rp == arct_approx)
    print("test_arctan (x = -0.5, p = 12) : \t PASSED")

    
def test_tan():

    #x = 0.9
    x = 0.9
    tan_python = math.tan(x)

    #p = 10
    p = 10
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = 0.9, p = 10) : \t PASSED")

    #p = 11
    p = 11
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = 0.9, p = 11) : \t PASSED")

    #p = 12
    p = 12
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = 0.9, p = 12) : \t PASSED")


    #x = 5
    x = 5
    tan_python = math.tan(x)

    #p = 10
    p = 10
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = 5, p = 10) : \t PASSED")

    #p = 11
    p = 11
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = 5, p = 11) : \t PASSED")

    #p = 12
    p = 12
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = 5, p = 12) : \t PASSED")
    

    #x = -2
    x = -2
    tan_python = math.tan(x)

    #p = 10
    p = 10
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = -2, p = 10) : \t PASSED")

    #p = 11
    p = 11
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = -2, p = 11) : \t PASSED")

    #p = 12
    p = 12
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = -2, p = 12) : \t PASSED")

    #p = 13
    p = 13
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = -2, p = 13) : \t PASSED")
    

    #x = -0.5
    x = -0.5
    tan_python = math.tan(x)

    #p = 10
    p = 10
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = -0.5, p = 10) : \t PASSED")

    #p = 11
    p = 11
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = -0.5, p = 11) : \t PASSED")

    #p = 12
    p = 12
    tan_python_rp = rp(tan_python, p)
    tan_approx = rp(tan(x), p)
    assert(tan_python_rp == tan_approx)
    print("test_tan (x = -0.5, p = 12) : \t PASSED")
    

test_arctan()
test_tan()
