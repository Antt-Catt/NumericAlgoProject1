# def rp(x,p):
#     k = x
#     i=0
#     while(k>0):
#         k = k//10
#         i+=1
#     return round(x, p-i)


#print(rp(1234.56789, 2))

# Pour obtenir la puissance de l'écriture scientifique
def sc_writing_pow(x):
    i = 0
    if x >= 1:
        while (x/(10**i) > 10):
            i += 1
        return i
    else:
        while (x*(10**i) < 1):
            i += 1
        return -i

def rp(x,p):
    i_sc = sc_writing_pow(x)
    x_sc = x / (10**i_sc)
    x_sc_r = round(x_sc,p-1)
    x_rp = x_sc_r * 10**(i_sc)
    return round(x_rp,p-i_sc)

def test_rp():
    x1 = 3.141592658
    x2 = 10507.1823
    x3 = 0.0001857563

    # p = 4
    p = 4
    
    x1_expected = 3.142
    x2_expected = 10510
    x3_expected = 0.0001858
    
    x1_rp = rp(x1,p)
    x2_rp = rp(x2,p)
    x3_rp = rp(x3,p)

    assert(x1_rp == x1_expected)
    assert(x2_rp == x2_expected)
    assert(x3_rp == x3_expected)

    print("test_rp (p = 4) : \tPASSED")

    # p = 6
    p = 6

    x1_expected = 3.14159
    x2_expected = 10507.2
    x3_expected = 0.000185756
    
    x1_rp = rp(x1,p)
    x2_rp = rp(x2,p)
    x3_rp = rp(x3,p)


    assert(x1_rp == x1_expected)
    assert(x2_rp == x2_expected)
    assert(x3_rp == x3_expected)

    print("test_rp (p = 6) : \tPASSED")

    return None

test_rp()

def nb_sgnf_numbers(x):
    print(x," :")
    x_str = str(x)
    cmp=0
    i=0
    while ( x_str[i]=='0' or x_str[i]=='.'):
        i+=1
    while i<len(x_str):
        if x_str[i]!='.':
            cmp+=1
        print("    i:", i, " cmp:",cmp)
        i+=1
    return cmp


    # #probleme pour x_2 et x_4 
    # i_sc = sc_writing_pow(x)
    # x_sc = x / (10**i_sc)
    # x_sc=str(x_sc)
    # print(x_sc)
    # if x_sc[-1]=='0':
    #     return 1
    
    # return len(x_sc)-1

def test_nb_sgnf_numbers():

    x_1=0.000125
    x_2=000012500.00
    x_5=12500.0
    x_3=00.01
    x_4= 00.010

    assert(nb_sgnf_numbers(x_1) == 3)
    assert(nb_sgnf_numbers(x_3) == 1)
    assert(nb_sgnf_numbers(x_2) == 6)
    assert(nb_sgnf_numbers(x_4) == 2)

test_nb_sgnf_numbers()

def add(x_1,x_2):
    p=6
    return rp(x_1,p)+rp(x_2,p)


