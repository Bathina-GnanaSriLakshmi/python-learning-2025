#To check whether the given string is palindrome or not
str = input("Enter string: ")
rev =""
length =0
for char in str:
    length += 1
for char in range(-1,-length-1,-1):
    rev += str[char]
if rev == str:
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")