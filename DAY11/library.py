#To develop Library system
n = int(input("Enter number of books: "))
d ={}
for i in range(n):
    key = input("Enter book name: ")
    value = int(input("No.of copies: "))
    a = 0
    d[key] = value
while a != "4":
    a = input("Enter 4 to exit and 3 to continue")
    name = input("Enter book name: ")
    if name in d and d[name] != 0:
        d[name] -= 1
        print("Book is provided")
    else:
        print("Book Not available")