# 2. What is wrong in the following code.
#
# L = [ ['John', [88,89,78] ],  ['Sam', [89,76,99] ],  ['Dev', [85,67,89] ] ]
# for name, m1,m2,m3 in L:
#      total = m1+m2+m3
#      print(name, total)

# if you check length of the list then it will be 2.
# it should be as accessed as m[0],m[1],m[2] so on

L = [ ['John', [88,89,78] ],  ['Sam', [89,76,99] ],  ['Dev', [85,67,89] ] ]
for name, m in L:
     total = m[0]+m[1]+m[2]
     print(name, total)

for name, [m1,m2,m3] in L:
     total = m1+m2+m3
     print(name, total)