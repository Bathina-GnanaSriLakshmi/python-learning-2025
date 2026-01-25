#To find student with highest score using nested dictionary
n = int(input("Enter number of students: "))
m = int(input("Enter numer of subjects: "))
d = {}
for i in range(n) :
    d2 = {}
    key = input(f"Enter student-{i+1} name: ")
    for j in range(m):
        key2 = input(f"Enter subject-{j+1} name: ")
        value2 = int(input("Enter marks: "))
        d2[key2] = value2
    d[key] = d2
print(d)
high = 0
for i in d:
    total = 0
    for j in d[i]:
        total += d[i][j]
    if total > high:
        high = total
        student = i
print(f"Highest marks are {high} scored by {student}")