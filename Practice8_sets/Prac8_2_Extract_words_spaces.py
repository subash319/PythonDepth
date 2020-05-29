# 2. From the following two strings, find all words common in both the strings. Extract words from the
# string by splitting on spaces.
#
# string1 = "Life has no remote, get up and change it yourself"
# string2 = "Life has no ctrl+Z"

string1 = "Life has no remote, get up and change it yourself"
string2 = "Life has no ctrl+Z"
s1 = set(string1.split())
s2 = set(string2.split())
print(s1.intersection(s2))
