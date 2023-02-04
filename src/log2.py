from decimal_ import rp
import math

def calc_log(p):
    res = 0
    for n in range(1, 1000000):
        if n % 2 == 0:
            res -= 1/n
        else:
            res += 1/n
    return rp(res,p)

#print(calc_log(20))

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

test_log()
