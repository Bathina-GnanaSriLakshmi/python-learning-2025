#To remove the duplicate elements from the list
l = list(map(str,input("Enter elements in the list: ").split()))
dup = []
for i in l:
    if i in dup :
        pass
    else :
        dup.append(i)
print(f"The list after deleting duplicate elements from the list is {dup}")