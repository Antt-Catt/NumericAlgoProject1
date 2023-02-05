import matplotlib.pyplot as plt
import numpy as np


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
    if x >= 1 or x <= -1:
        while (x/(10**i) > 10):
            i += 1
        return i
    elif x >= 0:
        while (x*(10**i) < 1):
            i += 1
        return -i
    else:
        while (x*(10**i) > -1):
            i += 1
        return -i
#Ecriture deciale reduite
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
    x4 = -4.0255941341
    x5 = -0.0856870465

    # p = 4
    p = 4
    
    x1_expected = 3.142
    x2_expected = 10510
    x3_expected = 0.0001858
    x4_expected = -4.026
    x5_expected = -0.08569
    
    x1_rp = rp(x1,p)
    x2_rp = rp(x2,p)
    x3_rp = rp(x3,p)
    x4_rp = rp(x4,p)
    x5_rp = rp(x5,p)
    
    assert(x1_rp == x1_expected)
    assert(x2_rp == x2_expected)
    assert(x3_rp == x3_expected)
    assert(x4_rp == x4_expected)
    assert(x5_rp == x5_expected)

    print("test_rp (p = 4) : \tPASSED")

    # p = 6
    p = 6

    x1_expected = 3.14159
    x2_expected = 10507.2
    x3_expected = 0.000185756
    x4_expected = -4.02559
    x5_expected = -0.0856870
    
    x1_rp = rp(x1,p)
    x2_rp = rp(x2,p)
    x3_rp = rp(x3,p)
    x4_rp = rp(x4,p)
    x5_rp = rp(x5,p)


    assert(x1_rp == x1_expected)
    assert(x2_rp == x2_expected)
    assert(x3_rp == x3_expected)
    assert(x4_rp == x4_expected)
    assert(x5_rp == x5_expected)

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

#On 'essaie' de chercher le nombre de chiffres significatifs
"""
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
"""
#On choisit 6 chiffres significatifs
def add(x_1,x_2):
    p=3
    return rp(x_1,p)+rp(x_2,p)

def mult(x_1,x_2):
    res = x_1 * x_2
    return rp(res,3)

def delta_add(x,y):
    return abs(((x+y)-add(x,y)))/abs(x+y)

#print(delta_add(12453035,1890692))

def delta_mult(x,y):
    return abs(((x*y)-mult(x,y)))/abs(x*y)

#print(delta_mult(12453035,1890692))


def question_5():
    max_delta_add=0
    max_delta_mult=0
    max_x=0
    max_y=0
    max_x_m=0
    max_y_m=0
    x=6213.1358
    # for x in range(1,1000000):
    for y in range(1,1000000):
        y=y/100
        d_a=delta_add(x,y)
        d_m=delta_mult(x,y)
        if d_a>max_delta_add:
            max_delta_add=d_a
            max_x=x
            max_y=y
        if d_m>max_delta_mult:
            max_delta_mult=d_m
            max_x_m=x
            max_y_m=y
    print("add : max : ",max_delta_add,"pour : ",max_x,"et",max_y)
    print("mul : max : ",max_delta_mult,"pour : ",max_x_m,"et",max_y_m)

# question_5()


# Y=np.arange(15,20,0.001)
# print(Y[0],Y[1],Y[2])
# # plt.plot(delta_add(6213.1358,Y))
# D_m = []
# for k in range(len(Y)):
#     D_m.append(delta_mult(6213.1358,Y[k]))
# print("ok")
# print(type(Y),type(D_m))
# plt.plot(Y,D_m)
# plt.ylabel('Delta_multiplication de x par y')
# plt.xlabel('variation de y, avec x fixé à 3213.1358')
# plt.show()
