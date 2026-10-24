secret_number = 42
total_attempts = 5
success = False

for attempts in range(1, 6):
    guess = int(input("Enter your number : "))
    remaining_number = total_attempts - attempts

    if guess == secret_number:
        print("Badhai ho aapne sahi number pahchan liya hai")
        success = True
        break
    elif guess > secret_number:
        print("thoda chota number sochiye :")
    else:
        print("thoda bada number sochiye :")

    if remaining_number > 0:
        print(f"{remaining_number} attempt left\n")

# YAHAN DHYAN DEIN: Yeh loop se bahar hai (bilkul left side mein)
if not success:
    print("sahi number! sahi number 42 tha.")
