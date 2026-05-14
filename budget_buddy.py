name = "Josiah"
budget_buddy = "Welcome to Budget Buddy"

weekly_income = 5000.75   
rent = 1200.00
groceries = 300.00
transportation = 100.00
is_student = True

total_expenses = rent + groceries + transportation
money_left = weekly_income - total_expenses

username = input("Please enter your name: ")
if username:
    name = username
weekly_income2 = input("Please enter your weekly income: ")
weekly_income2 = float(weekly_income2)
main_expenses = input("Please enter your main expenses: ")


introduction = f"\n{budget_buddy}, {username}! Here is your receipt! \n Weekly Income: ${weekly_income2} \n Total Expenses: ${total_expenses2} \n Money Left: ${money_left} \n Student Discount Applied: {is_student}\n"

print (introduction)