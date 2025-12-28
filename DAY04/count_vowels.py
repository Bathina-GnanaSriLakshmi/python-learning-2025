#To count number of vowels and characters in a string without using built-In functions
count_vowel=0
count_consonant = 0
str =input("Enter string: ")
for char in str:
    if char in "aeiouAEIOU":
        count_vowel += 1
    else:
        count_consonant += 1
print(f"No.of vowels = {count_vowel}")
print(f"No.of consonants = {count_consonant}")