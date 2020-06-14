# 2. Write a for loop to capitalize each string of this list. Use enumerate().

L = ['this', 'that', 'the', 'hello world']
for i, word in enumerate(L):
    print(f'{i}:{word}')
    L[i] = word.capitalize()
print(L)