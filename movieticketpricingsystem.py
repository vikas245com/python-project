age = int(input("Enter your age: "))
week_day = input("Enter your week day: ").lower()
if age < 12:
    ticket_price = 150
elif age  > 60:
    ticket_price = 120
else:
    ticket_price = 250

if week_day == "saturday" or week_day == "sunday":
    ticket_price = ticket_price + 50
coupen_code = input("Have y coupen code: (yes/no)").lower()
discount_price = 0 
if coupen_code == "yes":
    discount_price = ticket_price*0.10
final_price = ticket_price - discount_price
print(f"Final Ticket Price : {final_price}")

