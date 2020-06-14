# 10.  The following dictionary maps city codes to city names.
#
# cities = { '080':'Bengaluru', '044':'Chennai', '040':'Hyderabad', '011':'Delhi', '022':'Mumbai' }
# Create a set that contains the names of all cities whose code appears in the dictionary emp of question 8.

cities = { '080':'Bengaluru', '044':'Chennai', '040':'Hyderabad', '011':'Delhi', '022':'Mumbai' }
emp =  {  'id01' :  { 'name' : 'Dev', 'phone' : '08056771173'},
          'id02' :{ 'name' : 'Raj', 'phone' : '01176791193'},
          'id03' :  { 'name' : 'Ami', 'phone' : '08056774473'},
          'id04' :{ 'name' : 'Anita', 'phone' : '011767976193'},
          'id05' :  { 'name' : 'Sam', 'phone' : '08056771173'},
          'id06' :{ 'name' : 'Reena', 'phone' : '02276791193'},
          'id07' :  { 'name' : 'Akul', 'phone' : '08056774473'},
          'id08' :{ 'name' : 'Amar', 'phone' : '011767976193'}}
set_cities = {cities[value['phone'][:3]] for value in emp.values()}
print(set_cities)