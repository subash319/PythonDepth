# 11. The following for loop is written to delete all occurrences of an item from a list.
# Will it work properly? If not, what changes need to be made in this code.
#
# L = [1,2,3,2,4,5,2,2,2,7]
# x = 2
# for item in L:
#   if item == x:
#     L.remove(item)
# print(L)

L = [1,2,3,2,4,5,2,2,2,7]
x = 2
for item in L[:]:
  if item == x:
    L.remove(item)
print(L)