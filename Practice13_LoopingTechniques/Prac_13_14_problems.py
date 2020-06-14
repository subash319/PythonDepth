# 14.
#
# L = [1,2,-3,4,-5,-6, -8]
# for item in L[:]:
#        if item>=0:
#           L1.append(item)
# print(L)
# Instead of using this list copy solution for the problem that we saw in our lecture, we could do the following.
#
L = [1,2,-3,4,-5,-6, -8]
L1 = []
for item in L:
       if item>=0:
          L1.append(item)
L = L1
print(L)
L1.append(500)
print(L)
# What kind of problems can this solution create?