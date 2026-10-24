income = float(input("Enter your income: "))

food_expense , study_expense , travel_expense = map(float, input("Enter food, study, and travel expenses separated by space: ").split())
total_expenses = food_expense + study_expense + travel_expense 
remaining_balance = income - total_expenses
print(f"Your Income: {income}")
print(f"Your Total Expenses : {total_expenses}")
print(f"Your Remaining Balance : {remaining_balance}")
if total_expenses > income:
    print("warning: you are spending more than your budget!")
else:
    print("Great! you saved money this month ")
    
