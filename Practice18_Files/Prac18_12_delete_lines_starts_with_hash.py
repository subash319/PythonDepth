# 12. Write a program to delete lines that start with #.

with open('del_hash.txt','r+') as fr:
    lines = fr.readlines()
    fr.seek(0)
    for line in lines:
        if not line.startswith('#'):
            fr.write(line)
            print(line)