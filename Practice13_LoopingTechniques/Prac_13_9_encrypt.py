# 9. Encrypt the strings of this list by changing each letter of the string to next letter.

L = ['this', 'that', 'here', 'there']

for i,word in enumerate(L):
    new_word = ''
    for ind in range(len(word)):
        new_word += chr(ord(word[ind])+1)
        print(new_word)
    L[i] = new_word
print(L)
