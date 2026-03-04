from student import Student
import file_handler
import auth

def menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Students by Marks")
    print("6. View All Students")
    print("7. Exit")


if auth.login():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll: ")
            marks = input("Enter marks: ")
            s = Student(name, roll, marks)
            file_handler.add_student(s)
            print("Student added successfully!")

        elif choice == "2":
            roll = input("Enter roll to delete: ")
            file_handler.delete_student(roll)
            print("Student deleted!")

        elif choice == "3":
            roll = input("Enter roll to update: ")
            name = input("Enter new name: ")
            marks = input("Enter new marks: ")
            file_handler.update_student(roll, name, marks)
            print("Student updated!")

        elif choice == "4":
            roll = input("Enter roll to search: ")
            student = file_handler.search_student(roll)
            if student:
                student.display()
            else:
                print("Student not found!")

        elif choice == "5":
            students = file_handler.sort_students_by_marks()
            for s in students:
                s.display()

        elif choice == "6":
            students = file_handler.get_all_students()
            for s in students:
                s.display()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")