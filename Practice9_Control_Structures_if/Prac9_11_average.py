# 11. A list named L contains some integer values, write a line of code to find average of the
# list elements using ternary operator.

list_avg = list(range(0,100))
print(list_avg)
average = sum(list_avg)/len(list_avg) if len(list_avg) != 0 else None
print(average)