emp =  {  'id01' :  { 'name' : 'Dev', 'phone' : '08056771173'},
          'id02' :{ 'name' : 'Raj', 'phone' : '01176791193'},
          'id03' :  { 'name' : 'Ami', 'phone' : '08056774473'},
          'id04' :{ 'name' : 'Anita', 'phone' : '011767976193'},
          'id05' :  { 'name' : 'Sam', 'phone' : '08056771173'},
          'id06' :{ 'name' : 'Reena', 'phone' : '02276791193'},
          'id07' :  { 'name' : 'Akul', 'phone' : '08056774473'},
          'id08' :{ 'name' : 'Amar', 'phone' : '011767976193'}}

# This is a dictionary of all employees where key is the id of an employee and value is another dictionary
# that contains name and phone number of the employee. In the phone number, the
#
# first three characters represent the code of a city. Make a list of all those employees who have city code 080.

segregate_list = [value['name'] for key, value in emp.items() if value['phone'].startswith('080')]
print(segregate_list)