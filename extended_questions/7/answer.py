matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

N = len(matrix)
left_diagonal = []

for i in range(N):
    value = matrix[i][i]
    left_diagonal.append(value)

