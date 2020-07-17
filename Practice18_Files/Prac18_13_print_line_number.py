# 13. Write a for loop that prints the line number before each line of the file.

with open('del_hash.txt', 'r+') as fr:
    # lines = fr.readlines()
    # count = 0
    # fr.seek(0)
    # for line in lines:
    #     count += 1
    #     fr.write(str(count)+'   ' + line)
    for number, line in enumerate(open('del_hash.txt'), 1):
        print(number, line, end='')