def rp(x,p):
    k = x
    i=0
    while(k>0):
        k = k//10
        i+=1
    return round(x, p-i)


print(rp(1234.56789, 2))



