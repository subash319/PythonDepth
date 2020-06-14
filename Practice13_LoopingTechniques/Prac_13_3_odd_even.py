# 3. Given a list of integers, write a for loop that multiplies each odd number of the list by 2
# and divides each even number by 2. Use if else operator inside the loop.

list_integers = list(range(1, 10))
print(list_integers)
for i,num in enumerate(list_integers):
    list_integers[i] = list_integers[i] // 2 if num % 2 == 0 else list_integers[i]*2
print(list_integers)