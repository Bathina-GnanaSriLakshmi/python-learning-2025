#To find the union of two sets
s1 = set(map(str,input("Enter elements in set1: ").split()))
s2 = set(map(str,input("Enter elements in set2: ").split()))
s = []
for i in s1:
    s += [i]
for i in s2:
    s += [i]
print(set(s))