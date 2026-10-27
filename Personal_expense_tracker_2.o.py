print("--- Personal Expense Tracker 2.0 ---")
while True:
    print("\n 1. Add Expense")
    print("2. View All Expenses")
    print('3. Show total Expenses')
    print("4. Search Expense")
    print("5. Exit")
    choice = input("\nEnter choice: ")
    if choice == "1":
        expense_name = input("Enter your expenses name: ")
        expense_category = input("Enter your expenses category: ")
        try:
            expense_amount = float(input("Enter your expense amount: "))
        except ValueError:
            print("Error: please enter a valid number:")
            continue
        if expense_amount <= 0:
            print("Error: Amount zero ya negative nahi ho sakta hai: ")
        else:
            with open("expenses.txt", "a") as file:
                file.write(f"{expense_name}, {expense_category}, {expense_amount}\n")    
                print("Expense saved successfully!")
    elif choice == "2":
        print("\n --- View All Expenses ---")
        try:
            with open("expenses.txt" , "r") as file:
                lines = file.readlines()
                if not lines:
                    print("Expense file empty hai")
                else:
                    
                    for line in lines:
                       print(line.strip())
        except FileNotFoundError:
            print("Abhi tak koi expense save nahi hua hai! Pehle kuch add karein. ")
    elif choice == "3":
        total = 0 
        try:
            with open("expenses.txt" , "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    amount = float(parts[2])
                    total += amount
            print(f"Total Expenses: ₹{total:.2f}")
        except FileNotFoundError:
            print("abhi koi expense save nahi hua!")
    elif choice == "4":
        search_name = input("Enter expense name to search: ").strip()
        found = False
        try:
            with open("expenses.txt" , "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    if parts[0].lower() == search_name.lower():
                        print(line.strip())
                        found = True
            if not found:
                print("Expense not found:")
        except FileNotFoundError:
            print("abhi koi expense save nahi hua hai!")
    elif choice == "5":
        print("program band ho raha hai!, Exit")
        break
    else:
        print("invalid choice please enter a number between 1 and 5 \n")
