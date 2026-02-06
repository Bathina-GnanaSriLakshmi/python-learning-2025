#To check whether the list is sorted or not
n = int(input("Number of elements in the list: "))
l=[]
print("Enter element: ")
flag = True
for i in range(0,n):
    l.append(int(input()))
for i in range(1,n):
    if l[i]<l[i-1] :
        flag = False
        break
if flag:
    print("The list is sorted in ascending order")
else:
    print("The list is not in ascending order")