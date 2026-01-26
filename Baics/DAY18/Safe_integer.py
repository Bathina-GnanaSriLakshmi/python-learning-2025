try:
    num = int(input("Enter number: "))
    print(100/num)
except ZeroDivisionError:
    print("You can't divide number with zero ")
except ValueError:
    print("Give only integer as input")
else:
    print(f"input is {num}")
finally:
    print("Execution completed")