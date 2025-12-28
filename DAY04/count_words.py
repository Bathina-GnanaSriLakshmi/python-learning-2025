#To count number of words in the string
str = input("Enter string: ")
words = 0
for char in str:
    if char == " ":
        words += 1
print(f"Number of words in {str} = {words + 1}")