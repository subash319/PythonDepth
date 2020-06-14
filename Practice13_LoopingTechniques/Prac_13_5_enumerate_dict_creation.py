# 5. Write a program to create the following dictionary in which keys are numbers and values are their factorials.
# Don't use nested loops.

# D = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040}
# D = dict()
# for num in range(8):
#     if num == 0 or num == 1:
#         D[num] = num
#     else:
#         n = num
#         prod = 1
#         while n:
#             prod *= n
#             n -= 1
#         D[num] = prod
# print(D)
factorial = dict()
for i, num in enumerate(range(8)):
    if num == 0:
        factorial[num] = 1
    else:
        factorial[num] = factorial[num-1] * i
print(factorial)

