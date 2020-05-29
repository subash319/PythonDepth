# 7. How will you find out all the elements of list L1 that are not in L2.

L1 = [1,2,3,7]
L2 = [2,3,4,5]
L1_set = set(L1)
L2_set = set(L2)
print(L1_set.difference(L2_set))