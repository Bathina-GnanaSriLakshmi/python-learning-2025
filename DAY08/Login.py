#To build a simple login system
for i in range(0,3):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "Gnana Sri Lakshmi" and password == "qwerty123":
        print("Login completed")
    else:
        if i!=2:
            print("Try Again")
        else:
            print("Locked (only three attempts are allowed)")