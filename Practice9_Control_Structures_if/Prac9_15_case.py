# 15. Unlike some other languages, there are no switch case statements in Python.
# You can use the elif clauses or dictionary to achieve the functionality of a switch case.
#
# Write code using if..elif..else for printing the name of day depending on the value of a variable.
#
# value                           Action
#
#    0                               Print Sunday
#
#    1                               Print Monday
#
#    2                               Print Tuesday
#
#    3                               Print Wednesday
#
#    4                               Print Thursday
#
#    5                               Print Friday
#
#    6                               Print Saturday
#
#   Any other value        Print Invalid
#
# Write the same code using a dictionary.

val = int(input("Enter the value:"))
if val == 0:
    print('Sunday')
elif val == 1:
    print('Monday')
elif val == 2:
    print('Tuesday')
elif val == 3:
    print('Wednesday')
elif val == 4:
    print('Thursday')
elif val == 5:
    print('Friday')
elif val == 6:
    print('Saturday')
else:
    print('Invalid')

val_dict = {0:'Sunday', 1:'Monday', 3:'Wednesday' ,4:'Thursday',5:'Friday',6:'Saturday'}
#print(f'The corresponding day to val {val} is {val_dict[val]} {if val in val_dict else Invalid}')
print(f'The corresponding day to val {val} is {val_dict[val]}') if val in val_dict else print('Invalid')