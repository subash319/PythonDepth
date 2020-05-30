# marks = input('Enter marks - ')
# marks = int(marks)
#
# if marks >= 70:
#     grade = 'A'
# elif marks >= 60:
#     grade = 'B'
# elif marks >= 50:
#     grade = 'C'
# elif marks >= 40:
#     grade = 'D'
# else:
#     grade = 'E'
# print(grade)

# Suppose most of the students get E grade or D grade and very less students get A grade.
# It would be more efficient to rewrite this code the other way round.
#
# Refactor this code so that the more frequent conditions are written at the top of the if statement.

marks = input('Enter marks - ')
marks = int(marks)

if marks < 40:
    grade = 'E'
elif marks < 50:
    grade = 'D'
elif marks < 60:
    grade = 'C'
elif marks < 70:
    grade = 'B'
else:
    grade = 'A'
print(grade)