matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

n = len(matrix)
left_diagonal_sum = sum([matrix[i][i] for i in range(n)])
right_diagonal_sum = sum([matrix[i][n-i-1] for i in range(n)])
print(abs(left_diagonal_sum - right_diagonal_sum))