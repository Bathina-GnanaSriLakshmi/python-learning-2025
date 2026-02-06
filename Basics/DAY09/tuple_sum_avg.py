#To find the sum , average of elements
t = tuple(map(int, input("Enter elements: ").split()))
total = 0
count = 0

for i in t:
    total += i
    count += 1

average = total / count
print("Sum =", total)
print("Average =", average)
