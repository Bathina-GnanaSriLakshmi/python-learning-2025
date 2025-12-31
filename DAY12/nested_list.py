#To find total marks of the students using nested lists
n = int(input("Total number of students: "))
m = int(input("Number of stubjects: "))
marks = []
stu_marks = []
high = 0
for i in range(n):
    total = 0
    for j in range(m):
        a = int(input(f"Enter marks of student-{i+1} in subject-{j+1} : "))
        marks += [a]
        total += a
    stu_marks += [marks]
    marks = []
    if total>high:
        high = total
print(stu_marks)
print(f"highest score is{high}")
