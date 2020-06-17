# 7. Write a function that takes two arguments and returns sum, difference and product of those two arguments.

def calc_sum_diff(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2

s,d,p = calc_sum_diff(9,4)
print(s,d,p)