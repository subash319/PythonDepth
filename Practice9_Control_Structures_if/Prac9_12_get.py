# 12. We have seen that we can use the get method to avoid error while accessing a non-existent key.
#
# D = {'a':23, 'd':34, 'j':56}
# val = D['b']   # Raises Error
# val = D.get('b',0)  # Returns 0

# Instead of using get(), write a line of code that uses ternary operator
# to return a default value when the key is not present in the dictionary.

D = {'a':23, 'd':34, 'j':56}
#val = D['b']   # Raises Error
val = D['b'] if 'b' in D.keys() else None
print(val)
#val = D.get('b',0)  # Returns 0