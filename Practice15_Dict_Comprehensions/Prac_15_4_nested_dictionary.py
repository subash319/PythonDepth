#  4.  Change the dictionary comprehension that you wrote in previous question to create this nested dictionary.
#
# { 'Ted': {'Maths': 98, 'Physics': 88, 'Chemistry': 78},
#   'Sam': {'Maths': 67, 'Physics': 64, 'Chemistry': 67},
#   'Jim': {'Maths': 54, 'Physics': 78, 'Chemistry': 45},
#   'Rob': {'Maths': 88, 'Physics': 99, 'Chemistry': 79},
#   'Anu': {'Maths': 95, 'Physics': 78, 'Chemistry': 87}  }

names = ['Ted', 'Sam', 'Jim', 'Rob', 'Anu']
maths = [98, 67, 54, 88, 95]
physics = [88, 64, 78, 99, 78]
chemistry = [78, 67, 45, 79, 87]
dict_list = {name : {'Maths':maths_marks, 'Physics':physics_marks, 'Chemistry': chemistry_marks}
             for name,maths_marks,physics_marks,chemistry_marks in zip(names, maths, physics, chemistry)}
print(dict_list)