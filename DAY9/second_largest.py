#To find the second largest element 
t = tuple(map(int, input("Enter elements: ").split()))

largest = t[0]
second = t[0]

for i in t:
    if i > largest:
        second = largest
        largest = i

for i in t:
    if i != largest and i > second:
        second = i

print("Second Largest =", second)
