# 6. How can you perform order neutral equality tests in lists and strings using sets.
#
# L1 = [1,2,3,4]
# L2 = [2,3,1,4]
# These two lists L1 and L2 have same elements, only the order is different, so when you perform order neutral
# equality test on these 2 lists, they are considered equal.
# This test just checks whether both of them contain same elements.

L1 = [1,2,3,4]
L2 = [2,3,1,4]
L1_set = set(L1)
L2_set = set(L2)
print(L1_set.difference(L2_set))