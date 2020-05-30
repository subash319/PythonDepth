# 3.  Write a program that prompts the user to input his/her weight in kg and
# height in cms, and calculates the body mass index (BMI). BMI is calculated by
# dividing body weight in kg by square of height in meters.
#
# For example if weight is 70 kg, height is 170 cm,
#
# then BMI is 70/(1.7*1.7)  = 24.2
#
# Display the BMI and appropriate message according to the BMI.
#
# Underweight         < 18.5
#
# Normal weight     18.5 to 24.9
#
# Overweight           25 to 29.9
#
# Obese                     >=30

weight_kg = float(input('Enter the weight of user to calculate the BMI:'))
height_cm = float(input('Enter the height of user in CM:'))
height_met = height_cm/100
BMI = weight_kg/(height_met*height_met)
print(round(BMI, 1))
if BMI < 18.5:
    print('Underweight')
elif BMI <= 24.9:
    print('Normal Weight')
elif BMI <= 29.9:
    print('over Weight')
else:
    print('obese')
