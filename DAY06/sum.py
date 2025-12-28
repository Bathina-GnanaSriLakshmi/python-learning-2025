#To find the pair in the list with the given sum
sum = int(input("Enter the sum: "))
l = list(map(int,input("Enter elements in the list: ").split()))
a = 0
for i in l:
    a += 1
for i in range(0,a):
    for j in range(i+1,a):
        if i+j == sum:
            print(i,j)