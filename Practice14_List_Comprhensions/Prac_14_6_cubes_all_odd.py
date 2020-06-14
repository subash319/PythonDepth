# 6. This list comprehension creates a list of cubes of all odd numbers.
#
#   cubes = [ n**3  for n in range(5,21) if n%2!=0]
#      Can you write it without the if clause.

cubes = [n**3 for n in range(5, 21, 2)]
cubes_2 = [ n**3  for n in range(5,21) if n%2!=0]
print(cubes)
print(cubes_2)