#To check whether the list is palindrome or not
l = list(map(str,input("Enter the elements in the list: ").split()))
a = 0
flag = True
for i in l:
    a += 1
for i in range(0,int(a/2)):
    if i == 0:
        if l[0] != l[a-1]:
            flag = False
    if l[i] != l[-i-1]:
        flag = False
if flag:
    print("The given list is palindrome")
else:
    print("It is NOT a palindrome") 