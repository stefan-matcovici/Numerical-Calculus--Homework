def get_machine_precision():
    m = 1
    u = 10 ** -m
    while 1 + u != 1:
        m = m + 1
        u = 10 ** -m
    return m

