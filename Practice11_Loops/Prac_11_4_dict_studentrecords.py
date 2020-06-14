 # 4. Write a program to enter more student records inside the following dictionary.

students = { 105416 : { 'name':'John',
                        'age': 21,
                        'marks':  { 'Maths' :  89,
                                   'Physics' : 78,
                                   'Chemistry':91 }
                       },
             144547 : { 'name':'Dev',
                            'age': 23,
                        'marks': { 'Maths' :  88,
                                   'Physics' : 77,
                                   'Chemistry':98 }
                      },
             132399 : { 'name':'Mary',
                        'age': 22,
                        'marks':  { 'Maths' :  99,
                                    'Physics' : 87,
                                    'Chemistry':88 } ,
                      }
            }

Enter_more_records = False
print(Enter_more_records)
Enter_more_records = input("Do you want enter more records, Enter-More records, Anything-Quit")
print(Enter_more_records)
while not Enter_more_records:
    student_id = input("Enter the student Id:")
    student_name = input("Enter the name of the student:")
    student_age = input("Enter the age of the student:")
    student_marks_maths = input("Enter the maths marks:")
    student_marks_physics = input("Enter the physics marks:")
    student_marks_chemistry = input("Enter the chemistry marks:")
    student_record = dict()
    student_record['name'] = student_name
    student_record['age'] = student_age
    marks = {}
    marks['Maths'] = student_marks_maths
    marks['Physics'] = student_marks_physics
    marks['Chemistry'] = student_marks_chemistry
    student_record['marks'] = marks
    students[student_id] = student_record
    Enter_more_records = input("Do you want enter more records, Enter-More records, Anything-Quit")
    print(Enter_more_records)
print(students)