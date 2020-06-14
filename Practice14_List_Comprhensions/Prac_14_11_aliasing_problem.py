#  11.  This list L contains 6 references to the same list. How would you create this list L to avoid this
#  aliasing problem.
#
# L = [ [None]*3 ] * 6
# L = [ [None]*3 ] * 6
L = [[None]*3 for i in range(6)]
print(L)
L[1].append(1)
print(L)

