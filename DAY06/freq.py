#To find frequency of an element in a given list
n = input("Enter the element: ")
l = list(map(str,input("Enter elements in the list: ").split()))
freq = 0
for i in l:
    if i == n :
        freq += 1
print(f"The frequency of {n} in {l} is {freq}")