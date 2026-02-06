#To convert characters in lower case to uppercase in a string
str = input("Enter string: ")
result = ""
for char in str:
    if 'a' <= char <= 'z':
        result += chr(ord(char)-32)
    else:
        result += char
print(result)