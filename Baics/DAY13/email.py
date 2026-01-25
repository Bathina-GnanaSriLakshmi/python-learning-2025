#To generate email using names
names = list(map(str,input("Enter usernames : ").split(",")))
for i in names:
    email = '.'.join(i.split()).lower() + '@gmail.com'
    print(email)