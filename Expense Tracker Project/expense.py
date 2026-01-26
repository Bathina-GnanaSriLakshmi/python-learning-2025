expense = []
def add_expense():
    d = {}
    d["amount"] = int(input("Enter amount spent: "))
    d["category"] = input("Enter category: ")
    expense.append(d)
    with open("expense.txt","a") as f:
        f.write(f"Amount = {d['amount']} , Category = {d['category']} \n")
def total_expense():
    total = 0
    try:
        with open("expense.txt", "r") as f:
            for line in f:
                try:
                    a = int(line.split("=")[1].split(",")[0])
                    total += a
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File doesn't exist")
    print(f"Total expenses is {total}")

def highest_expense():
    high = 0
    try:
        with open("expense.txt", "r") as f:
            for line in f:
                try:
                    a = int(line.split("=")[1].split(",")[0])
                    if high<a:
                        high = a
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File doesn't exist")
    if high == 0:
        print("No expenses found")
    else:
        print(f"Highest expense is {high}")
def category_total():
    total_dict = {}
    try:
        with open("expense.txt","r") as f:
            for line in f:
                line = line.strip()
                if line=="":
                    continue
                cat = line.split(",")[1].split("=")[1].strip()
                amt = int(line.split("=")[1].split(",")[0])
                if cat in total_dict:
                    total_dict[cat] += amt
                else:
                    total_dict[cat] = amt
    except FileNotFoundError:
        print("File doesn't exist")
    print(total_dict)
op = 0
while op != 6:
    print("1.add expense 2.view all expenses 3.total expense 4.Highest expense 5.category wise total 6.Exit")
    try:
        op = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a number")
        continue
    if op == 1:
        add_expense()
        print("expense is added")
    elif op == 2:
        print("Expenses are: ")
        try:
            with open("expense.txt","r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No expenses recorded yet")
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