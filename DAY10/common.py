#To find the common elements in two lists
l1 = list(map(str,input("Enter elements in l1: ").split()))
l2 = list(map(str,input("Enter elements in l2: ").split()))
common = []
length_l1=0
length_l2=0
for i in l1:
    length_l1 += 1
for i in l2:
    length_l2 += 1
if length_l2>length_l1:
    t = length_l1
    length_l1=length_l2
    length_l2=t
for i in l1:
    for j in l2:
        if i==j:
            common += [i]
print(common)