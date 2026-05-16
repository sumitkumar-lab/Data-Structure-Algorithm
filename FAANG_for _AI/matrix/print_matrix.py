matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(len(matrix))

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j], end=" ")
#     print()    # new line after each row...

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

"""
Search target ?
"""
def matrixSearch(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return [i, j]
    return -1            
print(matrixSearch(matrix, 6))