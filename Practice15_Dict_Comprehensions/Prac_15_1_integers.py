# 1. Write a dictionary comprehension to create a dictionary which has integers
# from 1 to 20 as the keys, and values are squares of the keys.

d = {i: i*i for i in range(1, 21)}
print(d)
