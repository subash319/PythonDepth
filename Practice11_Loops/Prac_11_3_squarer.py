# 3. Write a program to create this dictionary in which the keys are numbers and values are their squares.
#
# { 1:1, 2:4, 3:9, 4:16, 5:25}

dict_squarer = dict()
for i in range(1,6):
    dict_squarer[i] = i*i
print(dict_squarer)