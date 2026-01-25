#To add new student to nested dictionary
d = {506 : {"name" : "gnana" , "cgpa" : 8.2 , "branch" : "CSE"},
     505 :  {"name" : "sri" , "cgpa" : 8.6 , "branch" : "cse"}
    }
d2 = {}
d2["name"] = input("Enter your name: ")
d2["cgpa"] = float(input("Enter your cgpa: "))
d2["branch"] = input("Enter your branch: ")
roll = int(input("Enter your roll number: "))
d[roll] = d2
print(d)