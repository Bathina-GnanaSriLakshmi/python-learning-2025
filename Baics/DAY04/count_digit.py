#To count number of digits,alphabets and special characters in a string
str = input("Enter string: ")
digit = 0
alpha = 0
spcl = 0
for char in str:
    if char in "0123456789" :
        digit += 1
    elif char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alpha += 1
    else :
        spcl += 1
print(f"No.of digits = {digit}")
print(f"No.of alphabets = {alpha}")
print(f"No.of special characters = {spcl}")