# 9. Write a statement to create a new string named code from three strings named name, dob and city.
#
# The string code contains every alternate character from string name(only upto 8th character),
# first two characters and last 2 characters from string dob and first three characters from string city.
# The string code will be 11 characters long.
#
# If
#
# name = 'Johny Abraham'
#
# dob = '09/11/1987'
#
# city = 'London'
#
# code will be 'JhyA0987Lon'
#
# If
#
# name = 'Marie Claire'
#
# dob = '12/04/1991'
#
# city = 'Paris'
#
# code will be 'MreC1291Par'

s = 'Johny Abraham'
dob = '09/11/1987'
city = 'London'
name = 'Marie Claire'
dob1 = '12/04/1991'
city1 = 'Paris'
# index_space = s.index(' ')
print(s[0:8:2]+dob[:2]+dob[-2:]+city[:3])
print(name[0:8:2]+dob1[:2]+dob1[-2:]+city1[:3])