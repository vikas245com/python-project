print("--- Personal expenses tracker---")
expense = []
while True:
    print("1. Add Expense: ")
    print("2. View All Expenses: ")
    print("3. Show Total Expenses: ")
    print("4. Exit")
    num = input("please select a number given: ")
    if num == "1":
        expense_naam = input("Enter your expenses name:")
        expense_category = input("Enter your expenses category:")
        expense_amount = float(input("Enter your expenses amount: "))
        exp = {
            "name" : expense_naam,
            "category" : expense_category,
            "amount" : expense_amount
        }

        expense.append(exp)
    elif num == "2":
        if not expense:
            print("no expenses added yet")
        else:
            for item in expense:
                print(item)
    elif num == "3":
        total = 0
        for item in expense:
            total += item["amount"]
        print(f"Total Expenses: {total}")
    elif num == "4":
        print("program band ho raha hai: ")
        break
    else:
        print("only 1 se 4 tak hee number add kare! ")
    

    