#To merge to lists manually
l1 = list(map(str,input("Enter elements in the list1: ").split()))
l2 = list(map(str,input("Enter elements in the list2: ").split()))
a=0
b=0
for i in l1:
    a += 1
for i in l2:
    b += 1
l3 = [0]*(a+b)
for i in range(0,a):
    l3[i] = l1[i]
for i in range(0,b):
    l3[i+a] = l2[i]
print(l3)