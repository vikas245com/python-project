secret_number = 27
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    guess = int(input("Enter your number : "))
    attempts += 1 
    if guess < secret_number:
        print("too low ")
    elif guess > secret_number:
        print("too high")
    else:
        print("correct!")
        print(f"aapne total {attempts} attempts me sahi guess kiye!")
        break
if attempts == max_attempts and guess != secret_number:
     print("game over")
     print(f"aapne poore {attempts} attempts use kar liye hai!")