#To swap keys and values in dictionary
n = int(input("Number of entries: "))
d ={}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
print(f"Original dictionary is {d}")
p = {}
for i in d:
    v = d[i]
    temp = v
    v = i
    i = temp
    p[i]=v
print(f"Dictionary after swapping: {p}")