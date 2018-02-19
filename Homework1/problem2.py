import random


def get_nonassociative_numbers():
    x, y, z = generate_random_numbers()
    while test_nonassociativty(x, y, z):
        x, y, z = generate_random_numbers()

    return x, y, z


def generate_random_numbers():
    return random.random(), random.random(), random.random()


def test_nonassociativty(x, y, z):
    return (x * y) * z == x * (y * z)
