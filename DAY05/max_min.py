#To find the max and min element in the list
n = int(input("Number of elements in the list: "))
l=[]
print("Enter element: ")
for i in range(0,n):
    l.append(int(input()))
a = l[0]
for i in range(0,n):
    if l[i]>a:
        a = l[i]
b = l[0]
for i in range(0,n):
    if l[i]<b:
        b = l[i]
print(f"The max element in the list {l} is {a}")
print(f"The min element in the list {l} is {b}")