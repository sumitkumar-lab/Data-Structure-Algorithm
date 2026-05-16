"""
This is the exact math that runs inside every Neural Network on the planet. 
When a layer in a neural network processes data, it is simply taking an 
Input Matrix ($X$) and multiplying it by a Weight Matrix ($W$).
"""
A = [[1,2],
     [3,4]]
"""
Your Task:
Before we write the giant multiplication loop, we need a reliable way to slice out a column.
Write a short snippet of code (a for loop or a list comprehension) that extracts Column 0 from 
Matrix B, resulting in a simple list: [5, 7].
"""
B = [[5,6],
     [7,8]]

def dot_product(vec_a, vec_b):
    return sum(a*b for a, b in zip(vec_a, vec_b))

# raw_of_a = [A[0][i] for i in range(len(A))]

# print(raw_of_a)

# col_of_b = [B[i][0] for i in range(len(B))]

# print(col_of_b)

# =========
# Our dot product helper function
def dot_product(vec_a, vec_b):
    return sum(a * b for a, b in zip(vec_a, vec_b))

def matrix_multiply(A, B):
    rows_A = len(A)   # number fo raws
    cols_B = len(B[0])   # number of column
    
    result_matrix = []
    
    # Outer loop: iterate through every row index in A
    for i in range(rows_A):
        new_row = []
        
        # Inner loop: iterate through every column index in B
        for j in range(cols_B):
            
            # Step 1: Extract row 'i' from Matrix A
            row_a = [A[i][p] for p in range(len(A[0]))]
            
            # Step 2: Extract column 'j' from Matrix B 
            # (Hint: Use your exact list comprehension, but swap '0' for 'j')
            col_b = [B[q][j] for q in range(len(B))]
            
            # Step 3: Calculate the dot product of row_a and col_b
            dp_value = dot_product(row_a, col_b)
            
            # Append the calculated number to our building row
            new_row.append(dp_value)
            
        # Append the finished row to our final matrix
        result_matrix.append(new_row)
        
    return result_matrix

# print(matrix_multiply(A, B))

#========== OR ==========#
def matrix_multiply(A, B):
    rows_A = len(A)
    cols_B = len(B[0])
    cols_A = len(A[0])
    
    result = []
    
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            val = sum(A[i][k] * B[k][j] for k in range(cols_A))
            row.append(val)
        result.append(row)
    
    return result


A = [[1,2,3],
     [4,5,6]]
B = [[2,4,6,8],
     [1,2,3,4],
     [2,5,8,3]]

# X = [[1.0, 2.0, 3.0, 4.0, 5.0],
#      [1.0, 2.0, 3.0, 4.0, 5.0]]
# Y = [150, 200, 250, 300, 350]

print(matrix_multiply(A, B))
