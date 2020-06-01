# 14. From the following set, make another set of all the names that start with an underscore.
#
# names = {'_num', 'var', 'product', '_add', '_sub', 'square'}

names = {'_num', 'var', 'product', '_add', '_sub', 'square'}
set_underscore = set()
for name in names:
    if str(name).startswith('_'):
        set_underscore.add(name)
print(set_underscore)