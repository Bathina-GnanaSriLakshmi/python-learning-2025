#To reverse a string without using built-in functions

str = input("Enter string: ")
length = 0 
for char in str:
    length += 1
for i in range(-1,-length-1,-1):
    print(str[i],end="")
