# 7. Write a program to find whether a year is leap year or not. A year is a leap year
# if it is divisible by 4, but not every year that is a multiple of 4 is a leap year.
# If a year is divisible by 100, then it is not a leap year unless it divisible by 400.
#
# Years 1980, 2040 are leap years as they are divisible by 4.
#
# Years 2000,  2400 , 1800, 1900, 2500 are divisible by 4, but since they are divisible
# by 100 we cannot say that all of them are leap years. Only those which are divisible by 400 will be leap years.
#
# Years 2000 and 2400 are leap years as they are divisible by 400, while 1800, 1900, 2500 are not leap years.

year_leap_check = int(input("Enter the year to check whether its leap year or not:"))
if year_leap_check % 4 == 0 and year_leap_check % 100 != 0:
    print(f'The Year {year_leap_check} is leap year')
elif year_leap_check % 100 == 0 and year_leap_check % 400 == 0:
    print(f'The Year {year_leap_check} is leap year')
else:
    print(f'The Year {year_leap_check} is not a leap year*')
