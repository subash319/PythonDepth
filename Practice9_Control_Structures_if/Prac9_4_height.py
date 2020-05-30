# 4. In the previous program, give the user an option to enter the height in
# inches or cms and weight in kgs or pounds. 1 inch = 2.54 cm
#
# 1 cm = 0.01 m
#
# 1 pound = 0.4535924 kg

height_choice = input('Enter your choice for height metric(c for cm, i for inch):')
height_to_be_converted = float(input('Enter the height of user:'))
weight_choice = input('Enter your choice for weight metric(k for kg, p for pound):')
weight_to_be_conv = float(input('Enter the weight of user:'))


if height_choice == 'c':
    height_met = height_to_be_converted/100
elif height_choice == 'i':
    height_met = height_to_be_converted * 0.0254  # 1 inch = 2.54 cm, 1 inch = 0.0254 met
else:
    print("You Entered a wrong option enter only c or i")

if weight_choice == 'k':
    weight_kg = weight_to_be_conv
elif weight_choice == 'p':
    weight_kg = height_to_be_converted * 0.454  # 1 pound = 454 gm, 1 pound = 0.454 kg
else:
    print("You Entered a wrong option enter only k or p")

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



