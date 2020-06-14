# 4. Write a for loop to print the elements of the following list in sorted order without duplicates.

L = [99,2,4,1,6,7,8,9,7,1,2,6,9,10,11,212]
for i in sorted(set(L)):
    print(i)