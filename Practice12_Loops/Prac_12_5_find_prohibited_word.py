# 5. You are given a text string and a list of prohibited words.
#
# text = 'This is crazy sample'
# prohibited_words = ['mad', 'lunatic', 'crazy']
# Use a for loop with else block, to find whether the text string contains
# any prohibited word. If you find a prohibited word display 'Found a prohibited word'.
# If the text string does not contain any prohibited word, then display 'No prohibited word in the list'.

text = 'This is crazy sample'
prohibited_words = ['mad', 'lunatic', 'crazy']
for word in text.split():
    if word in prohibited_words:
        print('Found a prohibited word')
        break
else:
    print('No prohibited word in the list') 