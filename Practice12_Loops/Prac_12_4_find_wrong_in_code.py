# 4. What is wrong in this program that is written to find a value in a list.

L = [1,2,4,5,6,8,9]
target = 3

found = False
for i,n in enumerate(L):
   if n  == target:
      found = True
      print(f'{target} found at index {i}')
      break
else:
    print(f'{target} not found')