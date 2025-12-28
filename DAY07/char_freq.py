#To write a function to count the frequency of the character
def char_frequency(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

s = input("Enter string: ")
ch = input("Enter character: ")
print("Frequency:", char_frequency(s, ch))
