def read_matrix(filename, separator=" "):
    with open(filename, "r") as f:
        return [list(map(float, line.split(separator))) for line in f]


def line_mapper(l):
    return [float(l[0]), int(l[1]), int(l[2])]


def read_system(filename, no_b=True):
    with open(filename, "r") as f:
        lines = f.readlines()
        b = []

        system_size = int(lines[0][:-1])

        if no_b:
            b = list(map(lambda x: float(x[:-1]), lines[2:2 + system_size]))
            a = list(map(line_mapper, list(map(lambda x: x[:-1].split(","), lines[2 + system_size + 1:]))))
        else:
            a = list(map(line_mapper, list(map(lambda x: x[:-1].split(","), lines[2:]))))

        return system_size, b, a
