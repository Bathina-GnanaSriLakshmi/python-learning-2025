#To check whether the number is palindrome or not
N = int(input("Enter Number: "))
a = N
b = N
c = N
digit = 0
flag = True
while   a>0:
    a //= 10
    digit += 1
for i in range(1,digit//2):
    first = c // pow(10, digit - 1)
    last = b%10
    if first!= last:
        flag = False
        break
    c = c%pow(10,digit-1)
    b = b // 10
    digit -= 2
if flag:
    print("It is a palindrome")
else:
    print("It is not a palindrome")   