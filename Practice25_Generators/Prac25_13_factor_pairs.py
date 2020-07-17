# 13. Write a program to generate factor pairs of a number. For example if the number is 500,
# the generator should generate these tuples.
#
# (1, 500) (2, 250) (4, 125) (5, 100) (10, 50) (20, 25)


def gen_fac(num):
    i = 1
    while i*i <= num:
        if num % i == 0:
            yield i, num//i
        i += 1


for tup in gen_fac(num=500):
    print(tup, end=' ')
