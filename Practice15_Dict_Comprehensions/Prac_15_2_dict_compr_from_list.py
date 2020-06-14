# 2. L = [2,4,6,7,5]
#
#     Write a dictionary comprehension to create the following dictionary from the list L.

# {2: [1, 2],
#  4: [1, 2, 3, 4],
#  6: [1, 2, 3, 4, 5, 6],
#  7: [1, 2, 3, 4, 5, 6, 7],
#  5: [1, 2, 3, 4, 5]
#  }
L = [2, 4, 6, 7, 5]
# L_dict = {[item : [ i for i in range(1, item)] for item in L}
L_dict = { n:[i for i in range(1, n+1)] for n in L}
print(L_dict)