 # 9. From this dictionary create a list of students whose total marks are more than 200.

students = {105416: {'name': 'John',
                     'gender': 'M',
                     'city': 'Paris',
                     'age': 21,
                     'marks': {'Maths': 89,
                               'Physics': 78,
                               'Chemistry': 91},
                     'is_sporty': True},

            144547: {'name': 'Dev',
                     'gender': 'M',
                     'city': 'London',
                     'age': 23,
                     'marks': {'Maths': 58,
                               'Physics': 57,
                               'Chemistry': 68},
                     'is_sporty': False},

            132399: {'name': 'Mary',
                     'gender': 'F',
                     'city': 'Paris',
                     'age': 22,
                     'marks': {'Maths': 99,
                               'Physics': 87,
                               'Chemistry': 88},
                     'is_sporty': True}
            }
# for student_id, dict in students.items():
#     sum =0
#     for mark in students[student_id]['marks'].values():
#         sum += mark
#     print("sum", sum)
#
#      # print(sum(students[student_id]['marks']))
list_stud_200 = [dict_record['name'] for student_id,dict_record in students.items()
                                     if sum(dict_record['marks'].values()) >200]
L = [student['name'] for student in students.values() if sum(student['marks'].values()) > 200 ]
print(L)
print(list_stud_200)