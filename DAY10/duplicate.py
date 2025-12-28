#To remove duplicates from the list without using set()
l = list(map(str,input("Enter elements in the list: ").split()))
s = []
dup = []
for i in l:
    if i in s:
        dup += [i]
    else:
        s += [i]
print(s)