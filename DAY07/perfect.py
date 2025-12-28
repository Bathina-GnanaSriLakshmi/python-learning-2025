#To write a functtion to check whether a number is perfect or not
def factors(n):
    for i in range(1,n):
        if n%i == 0:
            return n
n = int(input("Enter number: "))
l = [factors(n)]
sum = 0
for i in l:
    sum += i
if n == sum:
    print("It is a perfect number")
else :
    print("It is NOT a perfect number")