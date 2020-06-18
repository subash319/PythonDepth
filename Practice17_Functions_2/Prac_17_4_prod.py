# 4. Write a function that accepts any number of integers passed to it and returns their product.

def prod_any_numbers(*args):
    prod = 1
    for num in args:
        prod *= num
    return prod


print(prod_any_numbers(1, 2, 3, 4, 0))