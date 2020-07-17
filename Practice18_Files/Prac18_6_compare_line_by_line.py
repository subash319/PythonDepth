# 6. Write a program to compare two files line by line and report the line where they differ.

with open('comp1.txt','r') as f1:
    with open('comp2.txt', 'r') as f2:
        count = 0
        while True:
            line_first_file = f1.readline()
            line_second_file = f2.readline()
            count += 1
            if line_first_file != line_second_file:
                print(f'first_line:{line_first_file}\nsecond_line:{line_second_file} and count number is {count}')
                break
            if line_first_file == '' and line_second_file == '':
                print("Both the files are same")
                break


