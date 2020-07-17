# 7. Write a generator function that accepts a sequence and generates its numbers in reverse order.


def gen_rev(seq):
    for rev_index in range(len(seq)-1,-1,-1):
        yield seq[rev_index]


x = [1,2,3]
y = 'subash'
for ele in gen_rev(y):
    print(ele,end = ' ')