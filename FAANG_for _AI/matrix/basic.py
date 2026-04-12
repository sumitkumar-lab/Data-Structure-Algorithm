"""
Representation: How would you represent that exact $2 \times 3$ matrix above using standard Python lists? 
Assign it to a variable called matrix.

Measurement: Write two lines of code to programmatically find the number of rows and the number of 
columns in that matrix, assigning them to variables rows and cols.
"""
matrix = [[1,2,3],
          [4,5,6]]

rows = len(matrix)
cols = len(matrix[0])

print(rows)
print(cols)