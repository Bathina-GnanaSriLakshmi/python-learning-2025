#To find the expenses 
expenses = list(map(int,input("Enter expenses : ").split()))
sum_exp = sum(expenses)
print(f"Maximum expense : {max(expenses)}")
print(f"Minimum expense : {min(expenses)}")
print(f"sum of expenses : {sum_exp}")
print(f"average expense : {sum_exp/len(expenses)}")