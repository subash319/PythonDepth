# 13.
#
# data = [2,3,1,4,7,5]
# max_even = 0
# for item in data:
#    if item%2==0 and item>max_even:
#       max_even = item
# print(f'Largest even number is {max_even}')
# In this for loop, we are iterating over the items of a list and finding the largest even number.
#
# Make changes in this code so that you get the largest even number as well as its index.

data = [2,3,1,4,7,5]
max_even = 0
for index, item in enumerate(data):
   if item%2==0 and item>max_even:
      max_even = item
      idx = index
print(f'Largest even number is {max_even} at index {idx}')