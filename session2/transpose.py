def transpose(matrix):
    print([[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)