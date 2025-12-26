#To build an ATM style balance checker
bal = 0
def deposit(m,bal):
    bal += m
    print(f"Money of Rs{m} deposited successfully")
    return bal
def withdraw(m,bal):
    if m>bal:
        print("Insufficient Bank Balance")
        return bal
    else:
        bal -= m
        print(f"Money of Rs{m} is withdrawed successfully")
        return bal
o = "1"
while o != "4":
    print(" Menu: \n 1.deposit \n 2.withdraw \n 3.current Balance \n 4.Exit \n")
    o = input("Enter your option in numbers: ")
    if o == "1":
        m = int(input("Enter money to deposit: "))
        bal = deposit(m,bal)
    elif o == "2":
        m = int(input("Enter money to withdraw: "))
        bal = withdraw(m,bal)
    elif o == "3":
        print(f"The balance is Rs {bal}")
    elif o == "4":
        print(f"exiting...")
    else:
        print("Enter only valid options")