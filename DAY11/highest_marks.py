#To find the student with highest marks
d = {}
n = int(input("Enter number of students: "))
for i in range(n):
    student = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    d[student] = marks
high = 0
for i in d:
    if high<d[i]:
        high = d[i]

for i in d:
    if high == d[i]:
        print(i)