# D  = {'pen':10, 'pencil':5, 'eraser':8,  'sharpener':None, 'marker':15, 'ruler':None }
# In this dictionary, keys are names of fruits and values are their respective prices. For fruits
# that are out of stock, price is marked as None.
# Iterate over this dictionary and print only those fruits with their prices,
# that are in stock. Use ljust() and rjust() methods of str type to align your output.

D  = {'pen':10, 'pencil':5, 'eraser':8,  'sharpener':None, 'marker':15, 'ruler':None }
for item,price in D.items():
    if price != None:
        print(f'{item.ljust(8)}:{str(price).rjust(3)}')