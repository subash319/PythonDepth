# 1. The following dictionary has fruit names as keys and their prices as values.
#
# D = {'apple':100, 'banana':200, 'grapes':55, 'guava':60 }
#
#  Write a for loop that iterates over this dictionary and increases the price of a fruit by 10,
# if its price is less than 100, otherwise it decreases the price by 10.

D = {'apple':100, 'banana':200, 'grapes':55, 'guava':60 }
for fruit, price in D.items():
    if price > 100:
        D[fruit] -= 10
    else:
        D[fruit] += 10
print("Dictionary of fruits", D)