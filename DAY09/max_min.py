#To find the max,min elements in the tuple
t = tuple(map(int, input("Enter elements: ").split()))

max_val = t[0]
min_val = t[0]

for i in t:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum =", max_val)
print("Minimum =", min_val)
