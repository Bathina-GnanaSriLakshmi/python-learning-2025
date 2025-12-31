#To print only even numbers and search a value from the nested list
l = [[3,5,7,0],[5,6,4],[12,4,5]]
n = int(input("Enter element to search: "))
found = False
for i in l:
    for j in i:
        if j%2 == 0:
            print(f"{j}",end =" ")
        if j == n:
            found = True
if found:
    print("\nInteger Found")
else:
    print("\nInteger Not Found")