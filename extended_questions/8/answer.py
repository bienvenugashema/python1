matrix = [
    [11, 2],
    [4, 5]
]

N = len(matrix)
left_diagonal = []
start = N - 1
for i in range(N):
    value = matrix[i][start]
    start -= 1
    left_diagonal.append(value)

print(left_diagonal)