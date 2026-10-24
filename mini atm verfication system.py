atmpin = 1234
total_attempts = 3
for attempts in range(1 , 4):
    pin = int(input('Enter your 4 digit pin: '))
    remaining_pin = total_attempts - attempts 
    if pin == atmpin:
        print("access granted ! paise nikal sakte hain :") 
        break
    else:
        print(f"{remaining_pin} attempt left")

else:
    print("card blockd! 24 ghante baad try karein ") 

 