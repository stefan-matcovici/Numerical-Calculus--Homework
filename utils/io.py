def read_matrix(filename, separator=" "):
    with open(filename, "r") as f:
        return [list(map(float, line.split(separator))) for line in f]
