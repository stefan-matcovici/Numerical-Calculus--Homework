import random


def get_nonassociative_numbers():
    """ Finds 3 numbers x, y, z for which the equation (x*y)*z != x*(y*z) """
    x, y, z = generate_random_numbers()
    while test_multiplication_nonassociativity(x, y, z):
        x, y, z = generate_random_numbers()

    return x, y, z


def generate_random_numbers():
    """ Generates 3 random numbers within [0,1] """
    return random.random(), random.random(), random.random()


def test_multiplication_nonassociativity(x, y, z):
    """ Tests if x, y, z are not associative with regard to multiplication """
    return (x * y) * z == x * (y * z)

def test_sum_nonassociativity(x, y, z):
    """ Tests if x, y, z are not associative with regard to addition """
    return (x + y) + z == x + (y + z)
