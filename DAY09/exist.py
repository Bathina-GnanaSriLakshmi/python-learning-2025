#To check whether the element is present in tuple or not
t = tuple(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))
found = False

for i in t:
    if i == key:
        found = True
        break

if found:
    print("Element exists")
else:
    print("Element does not exist")
