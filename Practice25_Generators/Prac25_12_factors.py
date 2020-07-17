# 12. Write a generator function that accepts a number and generates its factors. For example -
#
# Factors of 500 are 1,2,4,5,10,20,25,50,100,125,250,500


def gen_fac(num):
    for i in range(1, num+1):
        if num % i == 0:
            yield i


for fact in gen_fac(num=500):
    print(fact, end=',')
