#To find fibanacci series by taking number of terms as input
N = int(input("Enter number: "))
sum =0
a = 0
b = 1
if N == 1:
    print("0")
elif N == 2:
    print("0,1")
else:
    print("0,1",end=",")
    for i in range (3,N+1):
        sum = a+b 
        print(sum,end=",")
        a = b
        b = sum
