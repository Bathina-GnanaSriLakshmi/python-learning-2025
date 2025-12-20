#To find the sum and product of digits in the number
N = int(input("Enter Number: "))
sum = 0
Product = 1

while N>0 :
    a = N%10
    sum = sum + a
    Product = Product * a
    N = int(N/10)

print(f"The sum of the digits is {sum}")
print(f"The product of the digits is {Product}")