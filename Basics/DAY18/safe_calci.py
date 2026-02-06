class InvalidOptionError(Exception):
    pass
op = 1
while(op != 5):
    print("1.Addition 2. Subtraction 3.Multiplication 4.Division 5.Exit")
    try:
        op = int(input("Enter option: "))
        if op>5:
            raise InvalidOptionError("Option should be in between 1 and 5")
    except ValueError:
        print("Invalid Input")
    except InvalidOptionError as e:
        print(e)
    try:
        a = int(input("Enter a value: "))
        b = int(input("Enter b value: "))
    except ValueError:
        print("Invalid Input")
    if op==1:
        print(a+b)
    elif op == 2:
        print(a-b)
    elif op == 3:
        print(a*b)
    elif op == 4:
        try:
            print(a/b)
        except ZeroDivisionError:
            print("b value cannot be zero")
    elif op == 5:
        print("Exiting...")
        exit()
        