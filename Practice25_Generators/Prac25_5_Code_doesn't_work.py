# 5. The following code does not work.
# Write a generator function named combine that yields values from the list, range function and the string.


L = [1,2,3,4,5]


def combine1(a, b, c):
    for i in a:
        yield i
    for i in b:
        yield i
    for i in c:
        yield i


for i in combine1(L, range(10,15), "ABCDEF"):
        print(i, end = ' ')