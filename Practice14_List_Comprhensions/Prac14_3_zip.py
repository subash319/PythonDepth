# 3. Create the list L using using zip instead of len and range.
#
# X=[1,2,3,4]
# Y=[5,6,7,8]
# L = [X[i]*Y[i] for i in range(len(X))]

X=[1,2,3,4]
Y=[5,6,7,8]
L = [x*y for x, y in zip(X, Y)]
print(L)