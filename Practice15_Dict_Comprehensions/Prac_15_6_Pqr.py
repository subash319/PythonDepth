
 # 6. From the dictionary d given in previous question, create a new dictionary that has all the key value pairs of
 # dictionary d, with all occurrences of pqr.com changed to pqr.org.


d  =   {'raj@xyz.com' : {'course':'Algorithms', 'city':'London'},
        'dev@abc.com' : {'course':'Painting', 'city':'Delhi'},
        'sam@pqr.com' : {'course':'Design Patterns', 'city':'London'},
        'jim@xyz.com' : {'course':'Networking', 'city':'Delhi'},
        'pam@abc.com' : {'course':'Algorithms', 'city':'Delhi'},
        'ray@abc.com' : {'course':'Painting', 'city':'London'},
        'anu@xyz.com' : {'course':'Algorithms', 'city':'London'},
        'bob@pqr.com' : {'course':'Data Structures', 'city':'Tokyo'},
        'ted@abc.com' : {'course':'Algorithms', 'city':'London'},
        'zen@abc.com' : {'course':'Painting', 'city':'London'} }
#d_new = {email.replace('pqr.com', 'pqr.org'):details for email,details in d.items() if email.endswith('pqr.com') }
d_new = {email if not email.endswith('pqr.com') else email[:-7] +'pqr.org' :details for email,details in d.items()}
print(d_new)