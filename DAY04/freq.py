# To find the frequency of a character in the string
str = input("Enter string: ")
ch = input("Enter character: ")
freq = 0
a = str
for char in a:
    if ch== char:
        freq += 1
print(f"Frequency of {ch} in {str} is {freq}")