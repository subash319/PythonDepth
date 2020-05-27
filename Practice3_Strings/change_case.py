# 7.  Make a new string s1, in which the first half of the string s is changed to
# uppercase and the second half to lower case.
#
# For example if string s is 'Hello World', string s1 is 'HELLO world'

s = 'Hello World'
s1 = s[:len(s)//2].upper() + s[len(s)//2:].lower()
print(s1)