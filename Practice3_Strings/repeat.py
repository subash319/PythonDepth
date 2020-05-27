# 2.  Make a string s1 from string s, in which the first 2 characters are repeated 5 times
# and the last character is repeated 3 times. For example if the string s is 'Hello World !',
# then the string s1 is 'HeHeHeHeHello World !!!'

s = 'Hello World !'
s1 = s[:2]*5 + s[:-1] + s[-1]*3
print(s1)