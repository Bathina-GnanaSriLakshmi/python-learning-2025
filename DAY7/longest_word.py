#To write a function to find longest word in the sentence
def long_word(a):
    num = 0
    str1 = ""
    n1 = 0
    t = "" 
    for i in a:
        t += i
        if i != " ":
            num += 1
        if i== " ":
            if num>n1:
                str1 = t
                n1 = num
            num = 0
            t = ""
    if num>n1:
        str1 = t
        n1 = num
    return str1,n1
a = input("Enter sentence: ")
t,num = long_word(a)
print(f"The longest word in the sentence is {t} with {num} letters")