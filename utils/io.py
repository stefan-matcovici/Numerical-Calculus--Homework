def read_matrix(filename, separator=" "):
    with open(filename, "r") as f:
        return [list(map(int, line.split(separator))) for line in f]
