#To normalize the user name
l = list(map(str,input("Enter string: ").split()))
for i in l:
    j = i.strip().lower()
    print(j)