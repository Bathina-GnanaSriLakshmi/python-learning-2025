#To write a function to find whether the number is prime or not
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
print("It is a Prime number" if prime(num) else "It is NOT a Prime number")
