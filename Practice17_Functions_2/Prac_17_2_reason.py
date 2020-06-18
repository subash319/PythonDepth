def result(*args, grade=False):
    total = sum(args)
    per = total / len(args)
    print(f'Total Marks = {total}, percentage = {per}%')
    if grade == False:
        return
    if per > 80:
        print('Grade A')
    elif per > 50:
        print('Grade B')
    else:
        print('Grade C')

result(90,90,90, grade = True)
result(90,90,90, True)

# The reason is all the arguments are packed in tuple, so True is taken as 1 and then total would be 271/4=67.75