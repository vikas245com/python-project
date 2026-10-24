correct_username = "vikas"
correct_password = 1234
username = input("Enter your username : ")
Password = int(input("Enter your password : "))
if username == correct_username and Password == correct_password:
    print("login successful") 
elif username == correct_username and Password != correct_password:
    print("wrong Password")
else:
    print("wrong Username") 