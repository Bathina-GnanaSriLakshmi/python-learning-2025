#To create dictionary from two lists
list1 = list(map(str,input("Enter keys: ").split()))
list2 = list(map(str,input("Enter values: ").split()))
d={}
a = 0
for i in list1:
    d[i] = list2[a]
    a += 1
print(d)