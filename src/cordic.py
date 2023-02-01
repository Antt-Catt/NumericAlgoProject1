import math
import decimal_ 

L=[math.log(2), math.log(1.1), math.log(1.01), math.log(1.001), math.log(1.0001), math.log(1.00001), math.log(1.000001)]

def ln(x):
    if(x>=10 or x<1):
        n = decimal_.sc_writing_pow(x)
        return ln(x*10**(-n))+n*math.log(10)


    k,y,p=0,0,1
    while(k<=6):
        while(x>=p+p*(10**(-k))):
            y= y+L[k]
            p=p+p*(10**(-k))
        k+=1
    return y+(x/p-1)


print(ln(0.15))
print(math.log(0.15))

def exp(x):
    if(x>=math.log(10) or x<1):
        n = decimal_.sc_writing_pow(x)
        return exp(x-n*math.log(10))*(10**(-n))
    k=0
    y=1
    while(k<=6):
        while(x>=L[k]):
            x=x-L[k]
            y=y+y*(10**(-k))
        k+=1
    return y+y*x

print(exp(15))
print(math.exp(15))