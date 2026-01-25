d = {}
d2={}
def add_student():
    d2 = {}
    roll_no = input("Enter roll no of student: ")
    d2["name"] = input("Enter name of student: ")
    d2["marks"] = int(input("Enter marks of student: "))
    d[roll_no] = d2
    print("Student is added in records")
def remove_student():
    new_d = {}
    student_roll = input("Enter student roll no who you want to remove: ")
    if student_roll in d:
        for i in d:
            if i != student_roll :
                new_d[i]= d[i]
        d.clear()
        for i in new_d:
            d[i] = new_d[i]
        print(f"student{student_roll} is deleted from records")
    else:
        print(f"Student named {student_roll} doesn't exist")
    
def update_marks():
    student_roll = input("Enter roll no of student whose marks should be updated")
    up_marks = int(input("Enter updated marks: "))
    if student_roll in d:
        for i in d[student_roll]:
            if i == "marks":
                d[student_roll]["marks"] = up_marks
choice = 0
print("Menu: ")
print(f"1.Add Student  2.Remove Student  3.Update Marks  4.Display all 5.Exit")
while choice != 5:
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        update_marks()
    elif choice == 4:
        print(d)
    elif choice == 5:
        print("Exit")
    else:
        print("Invalid choice!")