# Problem Statement:

# A school administrator is automating report-card generation. Write a Python function grade(marks) that uses Python conditional statements to take a student's marks as an integer and returns exactly one grade band using an if-elif-else chain:

# first class when marks are at least 40 and less than 80
# distinction when marks are at least 80 and at most 100
# fail when marks are below 40
# invalid marks when marks are above 100
# The function must handle the boundaries correctly: a mark of exactly 40 returns first class, a mark of exactly 80 returns distinction, a mark of exactly 100 returns distinction, a mark of 39 returns fail, and a mark of 120 returns invalid marks.

# Constraints & Requirements:

# Use a single if-elif-else chain so that only one branch runs.
# Use consistent indentation (four spaces) for every block body.
# The function must return exactly one grade band for any integer input.

def grade(marks):
    if 40 <= marks <= 80:
        return "First Class"
    elif 80 <= marks <= 100:
        return "Distinction"
    elif marks < 40:
        return "Fail"
    elif 100 < marks < 0:
        return "Invalid Marks"
    else:
        return "Enter Numbers Only"

mark = int(input("enter Mark: "))
print(grade(mark))