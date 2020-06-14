# 1.  Write a list comprehension to create a list that contains root of only positive numbers in this list.
#

L = [81, -9, 4, 16, -25, 64]
root_list = [item**0.5 for item in L if item >= 0]
print(root_list)

