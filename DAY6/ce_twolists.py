#To find the common elements in the two lists
l1 = list(map(str,input("Enter elements in list1: ").split()))
l2 = list(map(str,input("Enter elements in list2: ").split()))
len_l1 = 0
len_l2 = 0
for i in l1:
    len_l1 += 1
for i in l2:
    len_l2 += 1
temp = []
if len_l2>len_l1:
    temp = l2
    l2 = l1
    l1 = temp 
for i in l1:
    for j in l2:
        if i == j:
            print(i)
        