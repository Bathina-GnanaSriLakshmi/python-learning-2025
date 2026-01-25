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
    with open("expense.txt", "r") as f:
        for line in f:
            try:
                a = int(line.split("=")[1].split(",")[0])
                total += a
            except:
                    continue
    print(f"Total expenses is {total}")

def highest_expense():
    high = 0
    with open("expense.txt", "r") as f:
        for line in f:
            try:
                a = int(line.split("=")[1].split(",")[0])
                if high<a:
                    high = a
            except:
                    continue
    print(f"Highest expense is {high}")
def category_total():
    total_dict = {}
    with open("expense.txt","r") as f:
        for line in f:
            line = line.strip()
            if line==" ":
                continue
            cat = line.split(",")[1].split("=")[1]
            amt = int(line.split("=")[1].split(",")[0])
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
        with open("expense.txt","r") as f:
            contents = f.read()
            print(contents)
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