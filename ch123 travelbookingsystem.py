passenger_name = input("Enter passenger name : ")
age = float(input("Enter your age : "))
ticket_price = int(input("Enter ticket price : "))
available_money = float(input("Enter available money : "))
if age <= 5:
    discount = 50
elif 5 < age <= 12:
    discount = 30
elif 13 <= age <= 60:
    discount = 0
else:
    discount = 40
discount = (discount/100)*ticket_price
final_ticket_price = ticket_price - discount
ramaining_money = available_money - final_ticket_price
if available_money >= final_ticket_price:
    print("Booking successful ")
else:
    print("insufficient money ")
if age < 5:
    print("infant")
if age >= 60:
    print("senior citizen ") 
print("available money : " , available_money)  
print("total discount : " , discount)
print("final ticket price : " , final_ticket_price)
print("Remaining money : " , ramaining_money)
