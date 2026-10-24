print("--- Personal Expense Tracker Pro ---")
expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Show Total Expenses")
    print("5. Show Category-Wise Expenses")
    print("6. Delete Expense")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ").strip()
    
    if choice == "1":
        expense_name = input("Enter your expense name: ").strip()
        expense_category = input("Enter your expense category: ").strip()
        expense_amount = float(input("Enter your expense amount: "))
        
        expenses_item = {
            "expense_name": expense_name,
            "expense_category": expense_category,
            "expense_amount": expense_amount
        }
        expenses.append(expenses_item)
        print("Expense added successfully!\n")
        
    elif choice == "2":
        if not expenses:
            print("No expenses found!\n")
        else:
            print("\n--- All Expenses ---")
            for item in expenses:
                print(f"Name: {item['expense_name']}, Category: {item['expense_category']}, Amount: {item['expense_amount']}")
            print()
            
    elif choice == "3":
        if not expenses:
            print("No expenses added yet!\n")
        else:
            search_name = input("Enter expense name to search: ").strip()
            found = False
            for item in expenses:
                if item["expense_name"].lower() == search_name.lower():
                    print(f"-> Found! Name: {item['expense_name']}, Category: {item['expense_category']}, Amount: {item['expense_amount']}\n")
                    found = True
                    break
            if not found:
                print("Expense not found!\n")
                
    elif choice == "4":
        if not expenses:
            print("No expenses added yet!\n")
        else:
            total_expenses_value = 0
            for item in expenses:
                total_expenses_value += item['expense_amount']
            print(f"-> Total Expenses Value: {total_expenses_value}\n")
            
    elif choice == "5":
        if not expenses:
            print("No expenses added yet!\n")
        else:
            search_category = input("Enter category to show total (e.g., Food, Travel): ").strip()
            cat_total = 0
            found = False
            for item in expenses:
                if item['expense_category'].lower() == search_category.lower():
                    cat_total += item['expense_amount']
                    found = True
            if found:
                print(f"-> Total expense for category '{search_category}': {cat_total}\n")
            else:
                print("No expenses found for this category!\n")
                
    elif choice == "6":
        if not expenses:
            print("No expenses found to delete!\n")
        else:
            delete_expenses = input("Enter expense name to delete: ").strip()
            found = False
            for item in expenses:
                if item['expense_name'].lower() == delete_expenses.lower():
                    expenses.remove(item)
                    print("-> Expense deleted successfully!\n")
                    found = True
                    break
            if not found:
                print("Expense not found!\n")
                
    elif choice == "7":
        print("Program band ho raha hai. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 7.\n")
        