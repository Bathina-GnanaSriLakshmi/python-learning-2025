n = int(input("Enter year: "))
if n%4 == 0:
    if n%100 == 0:
        if n%400 == 0:
            print("Leap Year")
        else:
            print("Non leap year")
    else:
        print("Leap Year")
else:
    print("Leap Year")