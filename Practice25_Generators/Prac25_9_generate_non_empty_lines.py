# 9. Write a generator expression that generates all the non-empty lines in a file.


def line_gen(file):
    with open(file, 'r') as fr:
        for line in fr:
            if line != '\n':
                yield line


for line in line_gen('comp1.txt'):
    print(line,end='')

