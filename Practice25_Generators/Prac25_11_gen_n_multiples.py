# 11. Write a generator function to generate first n multiples of a number.
# # For example the first 5 multiples of 6 are 6 12 18 24 30.


def gen_n_multiples(num,mul_count):
    for i in range(1,mul_count+1):
        yield num*i


for i in gen_n_multiples(num=3,mul_count=10):
    print(i, end=' ')