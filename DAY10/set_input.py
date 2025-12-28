#To take input from user and store in set
n = int(input("Enter number of elements in the set:"))
s = set()
for i in range(0,n):
    s.add(input("Enter element{1}: "))
print(s)