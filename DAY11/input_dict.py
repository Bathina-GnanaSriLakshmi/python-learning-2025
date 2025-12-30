#To take dictionary as input from user
n = int(input("Enter no. of entries: "))
d = {}
for i in range(0,n):
    key = input("Enter key : ")
    value = int(input("Enter value: "))
    d[key] = value
print(d)