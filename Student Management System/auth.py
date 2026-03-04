ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False