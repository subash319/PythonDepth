# 5. Write a program to check whether a given sentence is a pangram or not.
# A pangram is a sentence that uses every letter of the alphabet at least once.
#
# Some examples of pangrams are -
#
# The quick brown fox jumps over the lazy dog.
#
# Pack my box with five dozen liquor jugs.
#
# Waltz, nymph, for quick jigs vex Bud.
# import string
# str_pangram_check = input('Enter the string to check pangram:')
# set_pangram_check = set(str_pangram_check)
# print(set_pangram_check)
# set_pangram_check.discard(' ')
# set_pangram_check.discard(',')
# set_pangram_check.discard('.')
# set_a_z = set(string.ascii_letters)
# print(set_pangram_check.difference(set_a_z))
# if not set_pangram_check.difference(set_a_z):
#     print("The string is pangrame")
# else:
#     print("The string is not pangrame")

s =  'The quick brown fox jumps over a lazy dog.'
if set('abcdefghijklmnopqrstuvwxyz') - set(s.lower()) == set():
    print('Pangram')
else:
    print('Not a pangram')