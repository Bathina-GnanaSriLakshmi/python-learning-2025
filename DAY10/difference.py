#To find the elements that are present in list A but not in list B
A = list(map(str,input("Enter elements in list A: ").split()))
B = list(map(str,input("Enter elements in list B: ").split()))
diff = []
for i in A:
    if i not in B:
        diff += [i]
print(diff)
