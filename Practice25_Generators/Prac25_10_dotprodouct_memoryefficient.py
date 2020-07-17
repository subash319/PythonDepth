# 10. The following code prints the dot product of 2 lists. Dot product is the sum of the
# products of the corresponding numbers in two sequences.

# How can you make this code memory efficient?

L1 = [5,10,15,20]
L2 = [1,2,3,4]
dot_product = sum((a*b for a,b in zip(L1, L2)))
print(dot_product)


# By removing the square brackets we can change the list comprehension to a generator expression.

