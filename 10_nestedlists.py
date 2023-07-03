"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(
s) of any student(s) having the second-lowest grade.

Note: If there are multiple students with the second-lowest grade, order their names alphabetically and print each
name on a new line.
"""

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([score, name])
students.sort()
minimum_score = students[0][0]
while students != [] and students[0][0] == minimum_score:
    students.pop(0)
if students:
    second_minimum_score = students[0][0]
    for x in students:
        if x[0] == second_minimum_score:
            print(x[1])
