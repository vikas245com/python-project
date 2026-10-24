correct_password = "admin123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    user_password = input("Enter password : ")
    attempts += 1
    if user_password == correct_password: 
        print("login successful")
        break 
    else:
        print("wrong password")
if attempts == max_attempts and user_password != correct_password: 
    print("Account Locked ") 