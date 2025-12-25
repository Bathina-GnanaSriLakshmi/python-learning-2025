#To write a function to check whether the number is armstrong or not
def armstrong(n):
    digit = 0
    arm = 0
    a = n
    while a>0 :
        digit = a%10 
        arm += digit ** 3
        a = a//10
    return arm
n = int(input("Enter number: "))
p = armstrong(n)
if p == n:
    print("The number is armstrong")
else:
    print("The number is not armstrong")