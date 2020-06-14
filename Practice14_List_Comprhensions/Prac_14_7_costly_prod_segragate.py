# 7. The following dictionary contains names of products as keys and prices as values.
#
#  prices = {   'pencil': 23,   'pen': 34,    'eraser':12,  'sharpener':13,  'marker':30}
# Write a list comprehension to create a list named costly_products that contains names
# of those products whose cost is more than 20.

prices = {'pencil': 23, 'pen': 34, 'eraser':12,  'sharpener':13,  'marker':30}
list_costly_prod = [item for item, price in prices.items() if price > 20]
print(list_costly_prod)