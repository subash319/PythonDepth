# 9.
# What problem will be there if you use the expression line[:-1] instead of line.rstrip().

with open('comp1.txt', 'r') as f:

    lines = [line.rstrip() for line in f ]
    print(lines)
# rstrip- strips the trailing element, Here it removes the trailing element
# But if you use the line[:-1] then the last line may not have the trailing new line character then there
# is a chance the last character may be missed
