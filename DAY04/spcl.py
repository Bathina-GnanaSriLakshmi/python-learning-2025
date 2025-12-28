#To replace space with special character

str = input("Enter string: ")
result = ""
for char in str:
    if char ==" ":
        result += "%"
    else :
        result += char
print(result)