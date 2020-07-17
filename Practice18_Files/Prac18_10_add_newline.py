# 10. Write a program to add an empty line after each line in the file.

with open('comp1.txt','r+') as fr:
       lines = [line+'\n' for line in fr]
       fr.seek(0)
       fr.writelines(lines)