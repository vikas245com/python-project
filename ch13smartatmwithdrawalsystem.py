def safe_atmwithdrawal():
    print("--- smart atm withdrawal ststem---")

    balance = 10000
    try:
        number = int(input("Enter your amount  "))
        if number <= 0:
            raise ValueError("amount zero /negative number nahi ho sakta hai")
        if number > balance:
            raise ValueError("Account mein itna balance nahi hai: ")
        balance = balance - number
        print(f"withdrawal successful bacha hua balance: {balance}")    

    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("aapka amount nikala jaa raha hai:")

if __name__ == "__main__":
    safe_atmwithdrawal() 

     

