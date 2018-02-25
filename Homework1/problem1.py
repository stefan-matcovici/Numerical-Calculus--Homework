def get_machine_precision():
    """ Returns the smallest positive number u, negative power of 10 (u=10**-m) that satisfies the property 1+u!=1 """
    m = 1
    u = 10 ** -m
    while 1 + u != 1:
        m = m + 1
        u = 10 ** -m
    return m - 1
