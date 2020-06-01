# 12. From this dictionary students, create two sets named toppers and champions. In the toppers set, add names of those
# students who have got more than 90 marks, and in the champions set, add names of those
# students who have more than 4 sports medals.

students = {   'id11' : { 'name': 'Amit',  'marks':97,  'sports_medals':0},
               'id12' : { 'name': 'Dev',   'marks':92,  'sports_medals':6},
               'id13' : { 'name': 'Ted',   'marks':81,  'sports_medals':2},
               'id14' : { 'name': 'Rob',   'marks':66,  'sports_medals':1},
               'id15' : { 'name': 'Sam',   'marks':56,  'sports_medals':1},
               'id16' : { 'name': 'Pam',   'marks':66,  'sports_medals':7},
               'id17' : { 'name': 'Ram',   'marks':98,  'sports_medals':9},
               'id18' : { 'name': 'Tim',   'marks':66,  'sports_medals':5},
           }

toppers = set()
champions = set()
for student in students.values():
    if student['marks'] > 90:
        toppers.add(student['name'])
    if student['sports_medals'] > 4:
        champions.add(student['name'])
print("Toppers", toppers)
print("champions", champions)
