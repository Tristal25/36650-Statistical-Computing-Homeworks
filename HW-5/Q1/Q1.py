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

X = [[10, 8],
     [2, 4],
     [1, 7]]
transpose(X)