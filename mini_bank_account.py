print("--- Mini Bank Account/ATM Simulator---")
account_holder = "" 
balance = 0.0
transactions = []
while True:
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Diposit Money")
    print("4. Withdraw Money")
    print("5. View Transaction History")
    print("6. Exit")
    choice = input("please select any given number:")
    if choice == "1":
        name = input("Enter account holder name: ")
        print("Account created successfully!")
        account_holder = name
    elif choice == "2":
        print(f"Current Balance: {balance}")
    elif choice == "3":
        diposit_amount = float(input("Enter your deposit money: "))
        balance += diposit_amount
        transactions.append(f"Deposited: {diposit_amount}")
        print(f"Current balance : {balance}")
    elif choice == "4":
        withdraw_amount = float(input("Enter your withdraw amount: "))
        if withdraw_amount <= balance:
            balance -= withdraw_amount
            transactions.append(f"withdrawn: {withdraw_amount}")
            print(f"withdraw successful! Current balance: {balance}")
        else:
            print("Insufficient Balance! Aapka account mein itne paise nahi hain.")
    elif choice == "5":
        if not transactions:
            print("No transaction history found!")
        else:
            for item in transactions:
                print(item)
    elif choice == "6":
        print("program band ho raha hai , Exit")
        break
    else:
        print("please 1 se 6 tak hee number enter karain!")






    