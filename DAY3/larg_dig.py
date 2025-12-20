# largest digit in the number
N = int(input("Enter number: "))
larg = 0
while N>0:
    a = N%10
    N //= 10
    if larg < a:
        larg = a
print(f"The largest digit in the number is {larg}")