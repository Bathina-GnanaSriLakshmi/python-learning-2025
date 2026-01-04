#To generate password checker
password = input("Enter Password: ")
check =  False
if any(ch.isdigit() for ch in password) and any(ch.isupper() for ch in password) and len(password)>= 8:
    check = True
if check:
    print("Password Updated")
else:
    print("Password should contain digit , alphabet and length > 8")