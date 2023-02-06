import math
from decimal_ import *

L=[math.log(2), math.log(1.1), math.log(1.01), math.log(1.001), math.log(1.0001), math.log(1.00001), math.log(1.000001)]

def ln(x):
    if(x>=10 or x<1):
        n = sc_writing_pow(x)
        return ln(x*10**(-n))+n*math.log(10)


    k,y,p=0,0,1
    while(k<=6):
        while(x>=p+p*(10**(-k))):
            y= y+L[k]
            p=p+p*(10**(-k))
        k+=1
    return y+(x/p-1)

def exp(x):
    if(x>=math.log(10) or x<1):
        n = sc_writing_pow(x)
        return exp(x-n*math.log(10))*(10**(-n))
    k=0
    y=1
    while(k<=6):
        while(x>=L[k]):
            x=x-L[k]
            y=y+y*(10**(-k))
        k+=1
    return y+y*x

# print(exp(15))
# print(math.exp(15))


# NB : valeur fausse pour p >= 13
def test_ln():

    #x = 0.5
    x = 0.5
    ln_python = math.log(x)

    #p = 10
    p = 10
    ln_python_rp = rp(ln_python, p)
    ln_approx = rp(ln(x), p)
    assert(ln_python_rp == ln_approx)
    print("test_arctan (x = 0.5, p = 10) : \t PASSED")

    #p = 11
    p = 11
    ln_python_rp = rp(ln_python, p)
    ln_approx = rp(ln(x), p)
    assert(ln_python_rp == ln_approx)
    print("test_arctan (x = 0.5, p = 11) : \t PASSED")

    #p = 12
    p = 12
    ln_python_rp = rp(ln_python, p)
    ln_approx = rp(ln(x), p)
    assert(ln_python_rp == ln_approx)
    print("test_arctan (x = 0.5, p = 12) : \t PASSED")


    #x = 5
    x = 5
    ln_python = math.log(x)

    #p = 10
    p = 10
    ln_python_rp = rp(ln_python, p)
    ln_approx = rp(ln(x), p)
    assert(ln_python_rp == ln_approx)
    print("test_arctan (x = 5, p = 10) : \t PASSED")

    #p = 11
    p = 11
    ln_python_rp = rp(ln_python, p)
    ln_approx = rp(ln(x), p)
    assert(ln_python_rp == ln_approx)
    print("test_arctan (x = 5, p = 11) : \t PASSED")

    #p = 12
    p = 12
    ln_python_rp = rp(ln_python, p)
    ln_approx = rp(ln(x), p)
    assert(ln_python_rp == ln_approx)
    print("test_arctan (x = 5, p = 12) : \t PASSED")

test_ln()
