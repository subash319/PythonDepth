# 1. The range function does not take a float value as a step. The call range(1, 10, 0.5) does not work.
# Write your own version of range that can accept a float value as the step.


def range_fraction(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    i = start
    # Generator stores the local state unlike the functions
    # They can be used as simple iterators
    # if you want the complex iterators we still need to write __iter__,__next__ methods
    while i < stop:
        yield i
        i += step

y = range_fraction(1, 10, 0.5)
for x in y:
    print(x)
print(sum(y))

for x in range_fraction(1, 5):
    print(x)

for x in range_fraction(5):
    print(x)

for x in range_fraction(1, 5, 0.5):
    print(x)
