#To count number of odd numbers and even numbers in the list
n = int(input("Number of elements in the list: "))
l=[]
print("Enter element: ")
for i in range(0,n):
    l.append(int(input()))
count_even = 0
count_odd = 0
for i in range(0,n):
    if l[i]%2 == 0:
        count_even += 1
    else:
        count_odd += 1
print(f"No.of even numbers is {count_even}")
print(f"No.of odd numbers is {count_odd}")