 # 7. A training on design patterns has to be delivered, all the enrolments are done.
 # The following dictionary contains the registration ids as the key and another dictionary as the value.

trainees = { '12AB' : { 'name': 'Ash', 'experince':12, 'language': 'C++' },
             '34CD' : {'name': 'Dev', 'experince':5, 'language': 'Python' },
             '55AB' : { 'name': 'Raj', 'experince':10, 'language': 'C++' },
             '67CD' : {'name': 'John', 'experince':3, 'language': 'Java' },
             '23ED' : {'name': 'Drek', 'experince':7, 'language': 'Python' },
             '35ED' : {'name': 'Amit', 'experince':4, 'language': 'Python' }
            }
# The trainer wants to provide hand-outs of sample programs in all the languages that trainees have chosen.
#  From this dictionary, find out a set of all the languages in which the trainer has to make programs.

set_lang = {value['language'] for value in trainees.values()}
print(set_lang)