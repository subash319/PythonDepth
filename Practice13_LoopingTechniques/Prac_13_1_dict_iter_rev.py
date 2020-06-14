# 1. Write a loop to iterate over the keys of this dictionary in reverse sorted order.
#

D = { 'apple':210, 'banana':100, 'grapes':90, 'mango':250, 'cherry':225, 'guava':80 }
for key in reversed(sorted(D.keys())):
    print(key, D[key])
