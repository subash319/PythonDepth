# 9.
# fruits = {'apple', 'banana', 'grapes'}
# veggies = {'potato', 'onion', 'cabbage'}
# stationery = {'pencil', 'eraser', 'sharpener', 'marker'}
# prices = {'pencil':10,'eraser':5,'sharpener':4, 'marker':20,'potato':30,
#          'onion':25, 'cabbage':22,'apple':90, 'banana':60, 'grapes':80}
# Write a for loop(use continue statement) to increase the price of all items by 10%, except fruits.
# Rewrite the loop without continue statement.

fruits = {'apple', 'banana', 'grapes'}
veggies = {'potato', 'onion', 'cabbage'}
stationery = {'pencil', 'eraser', 'sharpener', 'marker'}
prices = {'pencil': 10, 'eraser': 5, 'sharpener': 4, 'marker': 20, 'potato': 30,
          'onion': 25, 'cabbage': 22, 'apple': 90, 'banana': 60, 'grapes': 80}
# for item, value in prices.items():
#     if item in fruits:
#         continue
#     prices[item] += 0.1 * value
# print('prices:', prices)

for item, value in prices.items():
    if not item in fruits:
      prices[item] += 0.1 * value
print('prices:', prices)
