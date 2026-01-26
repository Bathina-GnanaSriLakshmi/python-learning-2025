l = ["apple","banana","orange","guava"]
try:
    i = int(input("Enter index: "))
    print(l[i])
except IndexError:
    print("Index Out Of Bound")
except ValueError:
    print("Invalid input")