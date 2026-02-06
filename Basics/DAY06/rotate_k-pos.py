#To rotate the list by k positions
k = int(input("Enter k value: "))
l = list(map(str,input("Enter elements in the list: ").split()))
a = 0
for i in l:
    a += 1
list2 =[0]*a
for i in range(0,a):
    list2[i]=l[i-k]
print(list2)