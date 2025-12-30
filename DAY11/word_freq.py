#To find the frequency of words in a sentence
string = input("Enter sentence: ").split()
d={}
for i in string:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)