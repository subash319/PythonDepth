# 10. Change your code written in the previous question, such that for all words that are to be censored,
# only the first letter is displayed. For the rest of the word, asterisks are displayed.
#
# Taking the example string s and list L of previous question, the string s should look like this after replacement.
#
# Here’s to the c**** ones. The misfits. The r*****. The t************. The ones who see things differently.
# They’re not fond of rules. And while some may see them as the c**** ones, we see genius.
# Because the people who are c**** enough to think they can change the world, are the ones who do.

s = '''Here’s to the crazy ones. The misfits. The rebels. The troublemakers.
The ones who see things differently. They’re not fond of rules.
And while some may see them as the crazy ones, we see genius.
Because the people who are crazy enough to think they can change the world, are the ones who do.'''

L = ['crazy', 'mad', 'rebels', 'lunatic', 'troublemakers', 'insane']

for word in L:
    s = s.replace(word, word[0]+(len(word)-1) * '*')
print(s)