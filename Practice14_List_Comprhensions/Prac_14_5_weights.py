# 5.  These three lists contain names, heights and weights of 6 people. Heights are in cms and weights are in kilograms.

names = ['John', 'Joe', 'Ted', 'Sam', 'Jack', 'Jill']
heights = [160, 152, 147, 167, 177, 182]
weights = [54, 60, 90, 77, 87, 67]

# Write a list comprehension to create a list of 2 element tuples where first element is the name,
# and second element is  the bmi of the person.
#
# BMI(body mass index) is calculated by dividing body weight in kg by square of height in meters.
#
# For example if weight is 70 kg, height is 170 cm,
#
# then BMI is 70/(1.7*1.7)  = 24.2
names = ['John', 'Joe', 'Ted', 'Sam', 'Jack', 'Jill']
heights = [160, 152, 147, 167, 177, 182]
weights = [54, 60, 90, 77, 87, 67]
list_bmi = [(name, (weight/((height*0.01)**2))) for name, weight, height in zip(names, weights, heights)]
print(list_bmi)