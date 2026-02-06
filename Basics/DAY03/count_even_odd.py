#To count even and odd digits in a number
N = int(input("Enter number: "))
digits = 0
a = N
sum_even = 0
sum_odd = 0
while a>0:
    digits += 1
    a //= 10
while digits>0:
    if digits%2 ==0:
        sum_even += N%10
    else :
        sum_odd += N%10
    digits -= 1
    N //= 10
print(f"The sum of even digits is {sum_even}")
print(f"The sum of odd digits is {sum_odd}")