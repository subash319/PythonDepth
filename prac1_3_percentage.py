# 3. Write a program which prompts the user to enter student name and his marks in
# 3 subjects and then calculates and displays his name and percentage

student_name = input("Enter the student name:")
marks_sub1 = float(input("Enter the marks in the first subject:"))
marks_sub2 = float(input("Enter the marks in the second subject:"))
marks_sub3 = float(input("Enter the marks in the third subject:"))
percentage = (marks_sub1+marks_sub2+marks_sub3)/3
print(f"The Student {student_name} secured a percentage of {percentage}")