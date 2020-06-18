# def display(L, start='', end=''):
#    for i in L:
#      if i.startswith(start) and i.endswith(end):
#          print(i, end=' ')
#
# display(dir(str), 'is', 'r')
# In the function definition of the function display(),
# make changes such that the user is forced to send keyword arguments for the last two parameters.

def display(L, *, start='', end=''):
   for i in L:
     if i.startswith(start) and i.endswith(end):
         print(i, end=' ')

display(dir(str), start = 'is', end = 'r')