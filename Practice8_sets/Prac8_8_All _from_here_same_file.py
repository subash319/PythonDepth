# 8. How will you find all the common characters in three strings s1, s2 and s3
# Ans: set(s1)&set(s2)&set(s3)
# You are given these 2 sets toppers and champions, where toppers is
# a set of roll numbers of academic toppers of the school and champions is a set of
# roll numbers of sports champions of the school.

toppers = set()
champions = set()
toppers  =  { 'id11', 'id23', 'id34', 'id45', 'id77', 'id12', 'id89', 'id56', 'id55', 'id70' }
champions  = { 'id19', 'id23', 'id78', 'id99', 'id79', 'id13', 'id56', 'id45', 'id80' }

# 9. From the set of toppers, remove student with rollnumber id12
toppers.remove('id12')
print('After removing id12:', toppers)

# 10. From the set of champions, add two students with roll numbers id45 and id19
champions.add('id45')
champions.add('id19')
print('After adding:', champions)

# 11. Find a set of all the toppers who are not champions
print(toppers.difference(champions))
# 12. Find a set of all the champions who are not toppers
print(champions.difference(toppers))
# 13. Find a set of all students who are champions as well as toppers
print(champions.intersection(toppers))
# 14. Find a set of all students who are either champions or toppers.

print(toppers | champions)