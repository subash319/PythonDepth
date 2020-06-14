# 2. Use a list comprehension to construct this list
#
#     [ '5x’, ’7x’, '9x', '11x', '13x', '15x', '17x' ]

list_comp = [ str(num)+'x' for num in range(5, 17) if num%2 != 0]
print(list_comp)