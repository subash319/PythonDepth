 # 10. Write a list comprehension that returns the sum of these two matrices M1 and M2.

M1 = [[1, 4, 8, 3],
      [2, 5, 6, 3],
      [7, 9, 5, 8]]

M2 = [[3, 5, 2, 3],
      [5, 2, 7, 9],
      [2, 8, 1, 8]]

sum_two_matrice = [[EleM1 + EleM2 for EleM1, EleM2 in zip(row1, row2)] for row1,row2 in zip(M1,M2)]
print(sum_two_matrice)