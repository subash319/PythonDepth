# 1. In the lecture on returning multiple values, we had written this function.
#
# def max_min_avg(L):
#    return max(L), min(L), sum(L)/len(L)
# Modify this function so that it can work with variable number of arguments.


def max_min_avg(*args):
    return max(args), mn(args), sum(args) / len(args)


mx, mn, avg = max_min_avg(10, 20, 30, 40, 5)
print(mx, mn, avg)
