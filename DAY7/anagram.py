#To write a function to check whether the given two strings are anagram or not 
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            return False
    return True

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagram" if is_anagram(s1, s2) else "Not Anagram")