expense = []
def add_expense():
    d = {}
    d["amount"] = int(input("Enter amount spent: "))
    d["category"] = input("Enter category: ")
    expense.append(d)
def total_expense():
    total = 0
    for i in expense:
        total += i["amount"]
    print(f"Total expense is {total}")
def highest_expense():
    if not expense:
        print("No expenses found")
        return
    high = 0
    for i in expense:
        if high < i["amount"]:
            high = i["amount"]
    print(f"Highest expense is {high}")
def category_total():
    total_dict = {}
    for i in expense:
        cat = i["category"]
        amt = i["amount"]
        if cat in total_dict:
            total_dict[cat] += amt
        else:
            total_dict[cat] = amt
    print(total_dict)
op = 0
while op != 6:
    print("Enter your option: ")
    print("1.add expense 2.view all expenses 3.total expense 4.Highest expense 5.category wise total 6.Exit")
    op = int(input("Enter your option: "))
    if op == 1:
        add_expense()
        print("expense is added")
    elif op == 2:
        print("Expenses are: ")
        print(expense)
    elif op == 3:
        total_expense()
    elif op == 4:
        highest_expense()
    elif op == 5:
        category_total()
    elif op == 6:
        print("Exiting...")
    else:
        print("Invalid Input. Select from the above given options")