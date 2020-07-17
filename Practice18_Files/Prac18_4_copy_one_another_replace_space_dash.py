# 4. Write a program to copy the contents of one file to another file such that each
# space in first file is replaced with a dash.

with open('hash.txt', 'r') as fr:
    with open('hash_replace_space_dash.txt', 'w') as fw:
        for line in fr:
            new_line = line.replace(' ', '-')
            fw.write(new_line)

