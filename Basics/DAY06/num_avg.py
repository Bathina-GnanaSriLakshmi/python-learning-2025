#To find the numbers in the list which are greater than average
l = list(map(int,input("Enter numbers in the list: ").split()))
a = 0
for i in l:
    a += 1
sum =0
for i in l:
    sum += i
avg = sum/a
print(avg)
for i in l:
    if avg<i :
        print(i)