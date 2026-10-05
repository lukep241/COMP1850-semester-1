# Worksheet 1.2: Task 1 Solution
import sys

grade = input("Enter a grade in the range 0 - 100: ")

if (grade.isdecimal() == False or (int(grade) < 0 or int(grade) > 100)):
    sys.exit("Error: Grade must be an integer between 0 and 100")
else:
    grade = int(grade)

if (grade <= 39):
    print(grade, "is a Fail")
elif (grade <= 69):
    print(grade, "is a Pass")
else:
    print(grade, "is a Distinction")
    



