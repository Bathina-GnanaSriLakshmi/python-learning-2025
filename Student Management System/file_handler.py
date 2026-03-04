from student import Student
FILE_NAME = "students.txt"
def add_student(student):
    with open(FILE_NAME, "a") as f:
        f.write(student.to_string() + "\n")
def get_all_students():
    students = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                students.append(Student.from_string(line))
    except FileNotFoundError:
        pass
    return students
def save_all_students(students):
    with open(FILE_NAME, "w") as f:
        for student in students:
            f.write(student.to_string() + "\n")
def delete_student(roll):
    students = get_all_students()
    students = [s for s in students if s.roll != roll]
    save_all_students(students)
def update_student(roll, new_name, new_marks):
    students = get_all_students()
    for s in students:
        if s.roll == roll:
            s.name = new_name
            s.marks = int(new_marks)
    save_all_students(students)
def search_student(roll):
    students = get_all_students()
    for s in students:
        if s.roll == roll:
            return s
    return None
def sort_students_by_marks():
    students = get_all_students()
    students.sort(key=lambda s: s.marks, reverse=True)
    return students