#To remove duplicate char in the string
str = input("Enter string: ")
result = ""
dele = ""
for char in str:
    if char in result:
        dele += char
    else:
        result += char
print(f"The string after deleting duplicate from {str} is {result}")
print(f"Duplicate char are {dele}")