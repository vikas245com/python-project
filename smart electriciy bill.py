unites = int(input("Enter your consumed units : "))
if unites < 100:
    rate = 5
elif unites < 300:
    rate = 7
else:
    rate = 10
meter_charge = 50
senier_citizen = input("kya aapke ghar mein koi senier citizen (yes/no): ").lower()
discount = 0
if senier_citizen == "yes":
    discount = 100
final_bill = unites*rate + meter_charge - discount
print("final electricity bill: " , final_bill)

