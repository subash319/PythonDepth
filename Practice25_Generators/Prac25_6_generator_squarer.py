# 6. Write a generator that generates squares of numbers.


def gen_squ():
    i = 1
    while True:
        yield i*i
        i += 1


for index,x in enumerate(gen_squ(),1):
    print(index,x, end=' ')
    if index == 1000:
        break