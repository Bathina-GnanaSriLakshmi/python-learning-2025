class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = int(marks)
    def to_string(self):
        return f"{self.name},{self.roll},{self.marks}"
    def from_string(data_str):
        name, roll, marks = data_str.strip().split(",")
        return Student(name, roll, marks)
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Marks: {self.marks}")
        print("-" * 20)