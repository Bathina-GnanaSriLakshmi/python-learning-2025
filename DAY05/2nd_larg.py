#To find the second largest element in the list
n = int(input("Number of elements in the list: "))
l=[]
print("Enter element: ")
for i in range(0,n):
    l.append(int(input()))
max = l[0]
for i in range(0,n):
    if l[i]>max:
        max = l[i]
max_2 = 0
for i in range(0,n):
    if l[i] != max:
        if max_2 < l[i] :
            max_2 = l[i]
print(f"The second largest number is {max_2}")
