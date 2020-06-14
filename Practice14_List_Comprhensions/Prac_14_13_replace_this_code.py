# 13. Write a list comprehension that can replace this code.

# pairs = []
# for n1 in range(4):
#      for n2 in range(4):
#           if n1!=n2:
#              pairs.append((n1,n2))

pairs = []
pairs = [(n1,n2) for n2 in range(4) for n1 in range(4) if n1!=n2]
print(pairs)