file_name = input("Enter File name: ")
try:
    with open(file_name,"r") as file:
        print(file.read())
except FileNotFoundError:
    print("File NOT found")