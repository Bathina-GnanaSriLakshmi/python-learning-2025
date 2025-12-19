l = input("Enter letter: ").lower()
if len(l)==1 :
    if l in "aeiou":
        print("The given letter is vowel")
    else :
        print("The given letter is consonant")
else:
    print("Only single character is allowed")