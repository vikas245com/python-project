print("--- Mini Banking System---")
balance = 1000
transactions = []
while True:
    print("1. Deposit Money")
    print("2. withdraw Money")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Enter your choice(1-5):")
    if choice == "1":
        Deposit_money = int(input("Enter your deposit Money:"))
        if Deposit_money <= 0:
            print("Invalid amount! Amount Zero ya nagetive nahi ho sakta hai!")
        else:
            balance += Deposit_money
            transactions.append(f"Deposited: {Deposit_money}")
            print(f"Money deposited successfully! Current Balance: {balance}")
    elif choice == "2":
        withdraw_money = int(input("Enter your withdraw money:"))
        if withdraw_money <= 0:
            print("Invalid amount!")
        elif withdraw_money > balance:
            print("not sufficient balance in your accocunt: ")
        else:
            balance -= withdraw_money
            transactions.append(f"withdrawn: {withdraw_money}")
            print(f"withdrawal successfully Current Balance: {balance}")
    elif choice == "3":
        print(f"Current Balance: {balance}")
    elif choice == "4":
        if not transactions:
            print("no trancsaction history found!\n")
        else:
            print("\n --- Transaction History ---")
            for t in transactions:
                print(t)
                print()
    elif choice == "5":
        print("program band ho raha hai. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1 to 5. ")
