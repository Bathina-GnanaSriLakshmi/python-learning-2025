#To reverse the elements in the list
n = int(input("Number of elements in the list: "))
l=[]
print("Enter element: ")
for i in range(0,n):
    l.append(int(input()))
print("List in reverse order: ")
for i in range(-1,-n-1,-1):
    print(l[i],end=" ")