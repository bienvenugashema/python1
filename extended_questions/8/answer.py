matrix = [
    [11, 2],
    [4, 5]
]

N = len(matrix)
right_diagonal = []
start = N - 1
for i in range(N):
    value = matrix[i][start]
    start -= 1
    right_diagonal.append(value)

print(right_diagonal)

# Sum of elements

print(sum(right_diagonal))