# 5. Enter a string and create 2 sets v and c, where v is a set of vowels present in the
# string and c is a set of consonants present in the string.

text = input("Enter your string please:")
vowel = set('aeiou')
string_c =  'BCDFGHJKLMNPQRSTVWXYZ'
consonats = set(string_c.lower())
print(consonats)
v = set(text)& vowel
c = set(text) & consonats
print(f'vowels:{v}\nconsonants:{c}')