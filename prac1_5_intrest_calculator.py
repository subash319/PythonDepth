# 5. Write a program that prompts the user to enter the values of principal,
# interest rate and time and computes simple interest.
# -Formula for simple interest
# simple interest = (principal * rate * time)  / 100

principal_amount = int(input("Enter the principal amount:"))
interest_rate = float(input("Enter the intrest rate per year:"))
period_time = float(input("Enter the time in years:"))
interest_amount = (principal_amount * interest_rate * period_time)/100
print(f"The interest amount calculated using the above inputs is: {interest_amount}")