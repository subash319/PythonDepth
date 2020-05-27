# Write a program that enters height in inches and displays it in feet and inches.
# 1 inch = 0.0833 feet/ 1feet = 12 inch

conversion_fact_inch_to_feet = 0.0833
no_of_inches = int(input("Enter the height in inches:"))
no_of_feet = no_of_inches*conversion_fact_inch_to_feet
print(f'The entered height {no_of_inches} inches is equal to {no_of_feet} feet')
