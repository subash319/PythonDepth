# 5. Write a function that takes in a variable number of strings and returns a list of all
# those strings in reverse form (use list comprehension).


def string_reverse_form(*args):
    st_rev = [s[::-1] for s in args]
    return st_rev

print(string_reverse_form('sub', 'ash', 'chan', 'dra', 'ell', 'uri'))