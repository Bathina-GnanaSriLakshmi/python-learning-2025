#To take n elements from user and store in tuples
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

t = tuple(lst)
print("Tuple:", t)
