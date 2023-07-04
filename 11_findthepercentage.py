"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

if query_name in student_marks:
    x = ((float(student_marks[query_name][0]) + float(student_marks[query_name][1]) + float(
        student_marks[query_name][2])) / 3)

print('%.2f' % x)