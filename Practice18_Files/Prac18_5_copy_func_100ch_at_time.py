# 5. Write a function copy_file that takes source and destination file names,
# and copies the file by copying 100 characters at a time.

def copy_file(src,dst):
    with open(src,'r') as fr:
        with open(dst,'w') as fw:
            while True:
                read_str = fr.read(100)
                if read_str == '':
                    break
                fw.write(read_str)


copy_file('hash.txt','copy_100charc.txt')