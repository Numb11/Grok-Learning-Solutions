expenses = input("Enter the expenses: ")
expenses = expenses.split()
amount = 0
for i in range(len(expenses)):
  amount = amount + int(expenses[i])
print (f"Total: ${amount}")
