#To find the sum of elements in the list
n = int(input("Number of elements in the list: "))
l =[]
print("Enter elements: ")
for i in range(0,n):
    l.append(int(input()))
sum = 0
for i in range(0,n):
    sum = sum + l[i]
print(f"The sum of the elements in the list{l} is {sum}")