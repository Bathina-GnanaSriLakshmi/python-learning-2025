#To solve the real world problem of student attendance system
roll = set(map(str,input("Enter student roll numbers: ").split()))
present = set(map(str,input("Enter present student roll no: ").split()))
total = 0
total_present = 0
for i in roll:
    total += 1
for i in present:
    total_present = 0
total_absent = total - total_present
absent = []
for i in roll:
    if i not in present:
        absent += [i]
print(f"Total present: {total_present}")
print(f"Total absent: {total_absent}")
print(f"absent students :{set(absent)}")