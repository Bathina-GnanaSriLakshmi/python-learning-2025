with open("file_basics.txt","r") as f:
    print(f.tell())
    print(f.read())
    print(f.seek(5))
    print(f.tell())
    print(f.read())