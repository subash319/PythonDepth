# 8. Write a program to replace each occurrence of a given word with another word.

word = 'Hex'
with open('comp1.txt', 'r+') as fr:
        s = fr.read().replace('SMALL', 'Subash')
        fr.seek(0)
        fr.write(s)