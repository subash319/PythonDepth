# 2. Write a generator function that behaves like enumerate.

# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in for loops or be converted into a list of tuples
# using list() method.


def enumerate_mod(iter_ble,start = 0):
    index = start
    for element in iter_ble:
        yield element,index
        index += 1


L = [10,20,30]
t = (8,9,10,11,12)

for element, ind in enumerate_mod(L):
    print(f'index:{ind} and element:{element}')

for element, ind in enumerate_mod(t,2):
    print(f'index:{ind} and element:{element}')


