# 12.  Transpose a matrix is a new matrix in which rows become columns and vice versa.
#
# M = [ [5,4,3,6],
#       [6,3,1,2],
#       [8,9,7,4]  ]
# Transpose of this matrix M is -
#
# T = [ [5,6,8],
#       [4,3,9],
#       [3,1,7],
#       [6,2,4] ]
# Write a list comprehension to create a list of lists that represents transpose of the matrix represented by M.

M = [ [5,4,3,6],
      [6,3,1,2],
      [8,9,7,4]  ]
# M_transpose = [[M[Ele][col] for Ele in range(3)]for col in range(4)]
M_transpose =  [[row[i] for row in M] for i in range(4)]
print(M_transpose)