# 4. Write an infinite generator that yields values 1 -1 2 -2 3 -3…….. Use it in a loop with break statement.


def inf_gen():
    num = 1
    while True:
        yield num
        yield -num
        num += 1


for x in inf_gen():
    if x == 100:
        break
    print(x, end=' ')