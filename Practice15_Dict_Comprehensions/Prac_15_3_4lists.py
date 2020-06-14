#
# names  = ['Ted', 'Sam', 'Jim', 'Rob', 'Anu']
# maths = [98,67,54,88,95]
# physics = [88,64,78,99,78]
# chemistry = [78,67,45,79,87]

# These 4 lists contain the names and marks of students in 3 subjects.
# Write a dictionary comprehension to create the following dictionary from the above 4 lists.

# { 'Ted': [98, 88, 78],
#   'Sam': [67, 64, 67],
#   'Jim': [54, 78, 45],
#   'Rob': [88, 99, 79],
#   'Anu': [95, 78, 87]  }

names = ['Ted', 'Sam', 'Jim', 'Rob', 'Anu']
maths = [98, 67, 54, 88, 95]
physics = [88, 64, 78, 99, 78]
chemistry = [78, 67, 45, 79, 87]
dict_list = {name : [math_marks, physics_marks, chemistry_marks] for name, math_marks, physics_marks, chemistry_marks in
    zip(names, maths, physics, chemistry)}
print(dict_list)