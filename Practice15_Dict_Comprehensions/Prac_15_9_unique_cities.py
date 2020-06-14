# 9. Find out the number of unique cities, whose code appears in the dictionary emp of previous question.

emp =  {  'id01' :  { 'name' : 'Dev', 'phone' : '08056771173'},
          'id02' :{ 'name' : 'Raj', 'phone' : '01176791193'},
          'id03' :  { 'name' : 'Ami', 'phone' : '08056774473'},
          'id04' :{ 'name' : 'Anita', 'phone' : '011767976193'},
          'id05' :  { 'name' : 'Sam', 'phone' : '08056771173'},
          'id06' :{ 'name' : 'Reena', 'phone' : '02276791193'},
          'id07' :  { 'name' : 'Akul', 'phone' : '08056774473'},
          'id08' :{ 'name' : 'Amar', 'phone' : '011767976193'}}

emp_unique_cities = {value['phone'][:3] for value in emp.values()}
print(len(emp_unique_cities))