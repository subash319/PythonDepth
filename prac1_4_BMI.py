# 4. Write a program that prompts the user to input his/her weight in kg and height in cms, and calculates
# the body mass index (BMI). BMI is calculated by dividing body weight in kg by square of height in meters.
# For example if weight is 70 kg, height is 170 cm,
# then BMI is 70/(1.7*1.7)  = 24.2

weight = float(input("Enter the user weight in kg :"))
height = float(input("Enter the height in cms:"))
height_in_meters = height/100
BMI = round(weight/(height_in_meters * height_in_meters), 1)
print("The BMI of the user is:", BMI)