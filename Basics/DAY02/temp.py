a = input("Enter the unit of temperature(C/F): ")
n = int(input("Enter the temperature: "))
if a == "C":
    f = ((n * 9)/5)+32
    print(f"The temperature in Fahrenheit is {f}")
elif a == "F":
    c =((n-32)*5)/9
    print(f"The temperature in Celsius is {c}")
else:
    print("Invalid Input")