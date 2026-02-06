#To check whether the given number is armstrong or not
N = int(input("Enter number: "))
a = N
sum = 0
while a>0:
    sum += pow(a%10,3)
    a = a//10
if sum == N:
    print("It is a Armstrong number")
else:
    print("It is NOT a Armstrong number")
