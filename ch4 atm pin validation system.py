pin = 1234
attempts = 0 
max_attempts = 3 
while attempts < max_attempts:
    atmpin = int(input("Enter your pin : "))
    attempts += 1
    if atmpin == pin:
        print("pin verified! Welcome")
        break
    else:
        bache_attempts = max_attempts - attempts
        print(f"wrong pin. {bache_attempts} attempts left ") 
if attempts == max_attempts and atmpin != pin:
    print("card Blocked for 24 hours!")



