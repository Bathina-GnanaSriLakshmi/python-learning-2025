n = int(input("Enter the number: "))
sqr = n*n
cub = n*n*n
a = input("Enter Sqr or Cub: ")
if a == "Sqr":
    print(f"The square of the number is {sqr}")
elif a == "Cub":
    print(f"The Cube of the number is {cub}")
else:
    print("Enter either Sqr or Cub")