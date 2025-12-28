#To build a menu driven Calculator
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
o = "exist"
while o != "exit":
    print("Menu: \n 1.add 2.substract 3.multiply 4.divide 5.exit\n")
    o = input("Enter operation from above given menu: ")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if o == "add":
        print(f"{add(a,b)}")
    if o == "substract":
        print(f"{substract(a,b)}")
    if o == "multiply":
        print(f"{multiply(a,b)}")
    if o == "divide":
        print(f"{divide(a,b)}")
    else:
        print("exiting...")
