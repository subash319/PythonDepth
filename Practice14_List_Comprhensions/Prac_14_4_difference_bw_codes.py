# 4. What is the difference between these three pieces of code.
#
#  (A)
#
# names = ['ted williams', 'John smith', 'tim jones']
# names = [ name.title()  for name in names ]
#  (B)
#
# names = ['ted williams', 'John smith', 'tim jones']
#       for name in names:
#           name = name.title()
#  (C)
#
# names = ['ted williams', 'John smith', 'tim jones']
# for i in range(len(names)):
#      names[i] = names[i].title()

# 4. In (A), the list comprehension creates and returns a new list object which is assigned to variable names.
# The new list contains all the names in title case.
#
# In (B), no new list object is created. The list is not changed because in each iteration,
# the changes are made to the loop variable name.
#
# In (C) also, no new list object is created but the list is changed. All the strings are titlecased.
#
# (A)  and (C) give the same result, but if there are multiple references to the original list, then
# they will not be updated if we use (A).