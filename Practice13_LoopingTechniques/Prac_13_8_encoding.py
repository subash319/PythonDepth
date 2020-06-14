# 8. In the lecture on for loop, we encrypted a message by replacing each letter by subsequent letter. Modify that
# program so that a character at even index is replaced by subsequent letter and a character at odd index
# is replaced by previous character.

message = 'Hi how are you, Thanks for coming'
emessage = ''
for i, ch in enumerate(message):
    if i % 2 == 0:
        emessage += chr(ord(ch)+1)
    else:
        emessage += chr(ord(ch)-1)
print(emessage)
