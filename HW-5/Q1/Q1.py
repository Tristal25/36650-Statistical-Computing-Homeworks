def transpose(matrix):
    # input: a matrix
    # output: matrix transpose
    trpos = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        trpos.append(row)
    return trpos
