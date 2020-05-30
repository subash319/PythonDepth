# 6. Anagram is a word or a phrase, formed by rearranging the letters of a different word or phrase.
# Some examples of anagrams are
#
# "binary" and "brainy"
#
# "silent" and "listen"
#
# "forty five"  and  "over fifty"
#
# "Madam Curie"  and  "Radium came"
#
# Write a program to find whether two phrases are anagrams.

phrase1 = input("Enter the first phrase:")
phrase2 = input("Enter the second phrase:")
if set(phrase1.replace(' ', '').lower()) == set(phrase2.replace(' ', '').lower()):
    print("phrases are anagram")
else:
    print("phrases are not anagram")
