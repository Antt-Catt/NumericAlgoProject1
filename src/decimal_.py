import matplotlib.pyplot as plt
import numpy as np

# sc_writing_pow : trouver l'écriture scientifique d'un entier
# Entrée : x réel
# Sortie : la puissance de 10 de l'écriture scientifique de x
def sc_writing_pow(x):
    i = 0
    if (x >= 1) or (x <= -1):
        while (abs(x/(10**i)) > 10):
            i += 1
        return i
    else:
        while (abs(x*(10**i)) < 1):
            i += 1
        return -i

# rp : Écriture décimale réduite
# Entrée : x un réel et p un entier
# Sortie : l'écriture réduite de x avec une précision de p décimales
def rp(x,p):
    i_sc = sc_writing_pow(x)
    x_sc = x / (10**i_sc)
    x_sc_r = round(x_sc,p-1)
    x_rp = x_sc_r * 10**(i_sc)
    return round(x_rp,p-i_sc)

# 'Comme il ne s’agit que d’une simulation, on supposera que p est faible.'
# On choisit alors p = 3 pour la suite

# add : simulation de l'addition
# Entrée : x_1 et x_2 deux réels
# Sortie : représentation décimale réduite de la somme de x_1 et x_2
def add(x_1,x_2):
    p = 3
    res = x_1 + x_2
    return rp(res,p)

# mult : simulation de la multiplication
# Entrée : x_1 et x_2 deux réels
# Sortie : représentation décimale réduite du produit de x_1 et x_2
def mult(x_1,x_2):
    p = 3
    res = x_1 * x_2
    return rp(res,p)

# delta_add : erreur relative de l'addition
# Entrée : x et y deux réels
# Sortie : erreur relative de x + y
def delta_add(x,y):
    return abs(((x+y)-add(x,y)))/abs(x+y)

# delta_mult : erreur relative du produit
# Entrée : x et y deux réels
# Sortie : erreur relative de x * y
def delta_mult(x,y):
    return abs(((x*y)-mult(x,y)))/abs(x*y)

# plot_delta_add : trouver x maximisant l'erreur relative pour y dans [0.01,100]
# Entrée : ()
# Sortie : x maximisant l'erreur relative
def choose_x():
    max_delta_mult = 0
    max_x_mult = 0
    x = 0.01
    while x < 10:
        y = 0.01
        while y < 100:
            d_m = delta_mult(x,y)
            if d_m > max_delta_mult:
                max_delta_mult = d_m
                max_x_mult = x
            y += 0.01
        x += 0.01
        print(x)
    return max_x_mult
    
# print(choose_x())
# max_x_mult = 0.15

# plot_delta_add : graphe de l'erreur relative de x + y avec y compris entre y_min et y_max
# Entrée : y_min et y_max réels
# Sortie : ()
def plot_delta_add(y_min,y_max):
    x = -51.391
    Y=np.arange(y_min,y_max,0.001)
    D_m = []
    for k in range(len(Y)):
        D_m.append(delta_add(x,Y[k]))
    plt.plot(Y,D_m)
    plt.ylabel('Delta_addition de x par y')
    plt.xlabel('variation de y')
    plt.show()
    return None

# plot_delta_add(1,100)
# plot_delta_add(45,60)

# plot_delta_mult : graphe de l'erreur relative de x * y avec y compris entre y_min et y_max
# Entrée : y_min et y_max réels
# Sortie : ()
def plot_delta_mult(y_min,y_max):
    x = 0.15
    Y=np.arange(y_min,y_max,0.001)
    D_m = []
    for k in range(len(Y)):
        D_m.append(delta_mult(x,Y[k]))
    plt.plot(Y,D_m)
    plt.ylabel('Delta_multiplication de x par y')
    plt.xlabel('variation de y')
    plt.show()
    return None

# plot_delta_mult(-100,100)
# plot_delta_mult(60,120)

# test_rp : tests de la fonction rp
# Entrée : ()
# Sortie : ()
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

# test_rp()
