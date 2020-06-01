# This code gives error if the user enters any non-numeric value. Rewrite the above two lines of code so that the user
# is forced to enter a numeric value for age, and that value should be less than or equal to 100.


age = (input('Enter your age : '))
while not age.isnumeric() or int(age) > 100:
    age = input('Wrong input\nEnter your age : ')
else:
    age = int(age)
    print(age)
