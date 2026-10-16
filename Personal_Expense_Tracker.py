expenses = []
while True:
    print("\n--- Personal Expense Tracker Menu ---")
    print("1. Add Expense:")
    print("2. View All Expenses:")
    print("3. Show Total: ")
    print("4. Search by Category:")
    print("5. Exit ")
    choice = input("Enter your choice:")
    if choice == "1":
        expense_name = input("Enter expense name:")
        category = input("Enter category: ")
        try:
            amount = float(input("Enter amount: "))
            expense = {
                "name" :expense_name,
                "category" : category,
                "amount" : amount
            }
        
            expenses.append(expense)
            print(f" '{expense_name}' successfully add ho gaya hai! ")

        except ValueError:
            print("Error> Kripya amount mein sirf numbers hee daale!")
    elif choice == "2":
        print("View All Expenses: ")
        if not expenses:
            print("Abhi koi expense add nahi hua:")
        else:
            for exp in expenses:
                print(f"Name: {exp['name']} | category:  {exp["category"]} | Amount:  {exp["amount"] }")
    elif choice =="3":
        print("Show Total:")
        if not expenses:
            print("koi expenses nahi hai :")
        else:
            total = sum(exp['amount'] for exp in expenses)
            print(f"Total Expenses Amount: {total}") 
    elif choice == "4":
        print("Search by Category:")
        if not expenses:
            print("search ke liye koi records nahi hain:")
        else:
            search_category = input("Enter category to search (e.g. , Food):").strip().lower()
            found = False
            for exp in expenses:
                if exp['category'].strip().lower() == search_category:
                    print(f"Name: {exp['name']} | Amount: {exp['amount']}")
                    found = True
    elif choice == "5":
        print("program band ho raha hai...")
        break
    else:
        print("Galt choice ! kripya 1 se 5 ke beech mein hee number daale. ")
