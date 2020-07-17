# 3. Write a generator function that takes a number n and then yields values from n to 1 and then again upto n.
# If n is 5, the values that are generated are : 5 4 3 2 1 2 3 4 5


# def gen_fun(num):
#     n = num
#     flag = 0
#     while True:
#         yield n
#         n = n-1 if flag == 0 else n+1
#         if n == 1:
#             flag = 1
#         if n > num:
#             break
# I like this model by lecturer, small code and easy to understand
def gfn(n):
    for i in range(n, 1, -1):
        yield i
    # First for loop should finish to execute this, so we have 5 4 3 2 1
    # Then the next generator works 1 2 3 4 5
    for i in range(1, n + 1):
        yield i


for i in gfn(5):
    print(i, end=' ')

# for x in gen_fun(10):
#     print(x)
