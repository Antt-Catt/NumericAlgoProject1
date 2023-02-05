from decimal_ import rp
import numpy as np
import matplotlib.pyplot as plt
import math

# calc_log : calcul la valeur approchée de log(2)
# Entrée : p entier
# Sortie : représentation décimale de log(2) à p décimales
def calc_log(p):
    res = 0
    for n in range(1, 1000000):
        if n % 2 == 0:
            res -= 1/n
        else:
            res += 1/n
    return rp(res,p)

# delta_log :
# Entrée : p entier
# Sortie : erreur relative de log(2)
def delta_log(p):
    return abs(((math.log(2))-calc_log(p)))/abs(math.log(2))

# plot_delta_log : graphe de l'erreur relative de log(2) avec p compris entre 1 et 20
# Entrée : ()
# Sortie : ()
def plot_delta_log():
    p = np.linspace(1,20,20) # p varie de 1 à 20
    log_approx = []
    for i in range(1,21):
        log_approx.append(delta_log(i))
    plt.plot(p,log_approx)
    plt.xlabel('valeur de p')
    plt.ylabel('delta_log(p) : erreur relative de log(2)')
    plt.show()
    return None

#plot_delta_log()

# test_log : tests de la fonction calc_log
# Entrée : ()
# Sortie : ()
# NB : représentation erronée à partir de p >= 5
def test_log():

    x = 2
    log_python = math.log(x)    

    # p = 1
    p = 1
    log_python_rp = rp(log_python,p)
    log_approx = calc_log(p)
    assert(log_python_rp == log_approx)
    print("test_log (p = 1) : \tPASSED")

    # p = 2
    p = 2
    log_python_rp = rp(log_python,p)
    log_approx = calc_log(p)
    assert(log_python_rp == log_approx)
    print("test_log (p = 2) : \tPASSED")

    # p = 3
    p = 3
    log_python_rp = rp(log_python,p)
    log_approx = calc_log(p)
    assert(log_python_rp == log_approx)
    print("test_log (p = 3) : \tPASSED")
    
    # p = 4
    p = 4
    log_python_rp = rp(log_python,p)
    log_approx = calc_log(p)
    assert(log_python_rp == log_approx)
    print("test_log (p = 4) : \tPASSED")

    return None

#test_log()
