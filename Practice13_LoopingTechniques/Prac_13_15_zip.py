# 15.Write a program that displays the following output from the above data. Use zip in for loop to iterate over the
# lists.
#
#
#
# John
#
# --------------------------------------------------
#
# Physics      100  40   90
#
# Chemistry   80  25   78
#
# Maths       100   40   87
#
# Biology       75   20   67
#
# Total = 322
#
# Percentage = 90.70
#
# --------------------------------------------------
#
# Sam
#
# --------------------------------------------------
#
# Physics     100   40   95
#
# Chemistry   80  25   76
#
# Maths       100   40   78
#
# Biology       75   20   57
#
# Total = 306
#
# Percentage = 86.20
#
# --------------------------------------------------
#
# Dev
#
# --------------------------------------------------
#
# Physics      100  40   80
#
# Chemistry   80  25   69
#
# Maths        100  40   59
#
# Biology     75  20   45
#
# Total = 253
#
# Percentage = 71.27
#
# --------------------------------------------------
D = { 'John' :  [90,78,87,67] ,
          'Sam' :  [95,76,78,57] ,
          'Dev' :  [80,69,59,45]
        }
subjects = ['Physics', 'Chemistry', 'Maths', 'Biology']
max_marks = [100, 80, 100, 75]
pass_marks = [40, 25, 40, 20]
# print(list(zip(D.items(),subjects,max_marks,pass_marks)))
for (name,marks) in D.items():
    print(name)
    print('-' * 50)
    total,sum_max_marks = 0,0
    for mark,subject,max_mark,pass_mark in zip(marks,subjects,max_marks,pass_marks):
        print(f'{subject:10} {max_mark:4} {pass_mark:4} {mark:5}')
        total += mark
        sum_max_marks += max_mark
        per = (total/sum_max_marks)*100
    print(f'Total = {total:3}')
    print(f'Max Marks = {sum_max_marks:3}')
    print(f'Percentage = {per:4.2f}')
    print('-' * 50)