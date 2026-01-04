#To remove the special characters from the string
string = input("Enter string: ")
for ch in string:
    if ch.isalnum():
        print(ch,end = "")