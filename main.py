
expense = [
 {
 "category": "Food",
  "amount": 2500
 },
{
 "category": "Transport",
  "amount": 1200
 },
{
 "category": "Shopping",
  "amount": 3000
 },
{
 "category": "Food",
  "amount": 1500
 },
{
 "category": "Rent",
  "amount": 8000
 },
 {
 "category": "Entertainment",
  "amount": 2000
 }
]

print("Expense Report:\n", expense)



#Total Expenses Summation
total_expense = 0
for item in expense:
    total_expense += item["amount"]
print('\n')
print("Total Expenses: ", total_expense)
print('\n')


# #Category Wise Expense Calculation
category_wise_expense = {}
for item in expense:
    Category = item["category"]
    Amount = item["amount"]
    
    if  Category in category_wise_expense:
        category_wise_expense[Category] += Amount
    else:
        category_wise_expense[Category] = Amount
    print("Category Wise Expense: ", category_wise_expense)
print('\n')  
    
    
#Lets Compare with Income. Check Savings
income = 70000
savings = income - total_expense
if savings > 0:
    print('My Savings:', savings,"Taka")
elif savings == 0:
    print('No Savings, No Loss.')
else:
    print('Loss:', abs(savings),"Taka")
    


    
#Highest Expense Category in My Dictonary
highest_expense_category = None
highest_expense_amount = 0
for category,amount in category_wise_expense.items():
    if amount > highest_expense_amount:
        highest_expense_amount = amount
        highest_expense_category = category
print("\nHighest Expense Category:\n",highest_expense_category, "Amount:", highest_expense_amount, "Taka")
