# 9. Write a loop to censor certain words in a text by replacing them with asterisks.
#     The words to be replaced are given in a list.  Here is an example -

s = '''Here’s to the crazy ones. The misfits. The rebels. The troublemakers.
The ones who see things differently. They’re not fond of rules.
And while some may see them as the crazy ones, we see genius.
Because the people who are crazy enough to think they can change the world, are the ones who do.'''
# s = '''Here’s to the crazy ones. The misfits The rebels The troublemakers
# The ones who see things differently. They’re not fond of rules.
# And while some may see them as the crazy ones, we see genius.
# Because the people who are crazy enough to think they can change the world, are the ones who do.'''

L = ['crazy', 'mad', 'rebels', 'lunatic', 'troublemakers', 'insane']
for word in L:
      s = s.replace(word, len(word) * '*' )
print(s)
