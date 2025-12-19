marks = int(input("Enter marks for 100: "))
if marks>100:
    print("Enter valid marks.")
elif marks>90:
    print("Grade A")
elif marks>80:
    print("Grade B")
elif marks>70:
    print("Grade c")
elif marks>60:
    print("Grade D")
else :
    print("You failed in exam. Better Luck next time")