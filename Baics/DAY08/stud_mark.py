#To build a student mark analyzer
name = input("Enter name of the student: ")
l = list(map(int,input("Enter marks of three subjects: ").split()))
def total(l):
    tot = 0
    for i in l:
        tot += i
    return tot
def fail(l):
    grade = "passed"
    for i in l:
        if i < 35:
            grade = "failed"
    return grade
def avg(l):
    av = total(l)/3
    return av
print(f"Total marks scored : {total(l)}")
print(f"student {fail(l)} in exam ")
print(f"Average : {avg(l)}") 