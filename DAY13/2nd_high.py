#To find the second highest number in the list
l =list(map(int,input("Enter numbers: ").split()))
a =[]
for i in l:
    if i not in a:
        a.append(i)
a.sort()
print(a[1])
