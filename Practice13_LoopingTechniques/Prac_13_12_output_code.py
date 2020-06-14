# 12. What will be the output of this program -
#
L = [1,2,-3,4,-5,-6,8]
# [1,2,4,-6,8]
# 0 1, 1 2, 2 -3, 3 -5, 4 8
i = 0
while i < len(L):
   print(i, L[i])
   if L[i] < 0:
      L.remove(L[i])
   i+=1
print(L)