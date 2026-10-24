customer_name = input("Enter your name : ")
units_consumed = int(input("Enter you consumed unit : "))
per_unit_rate = int(input("Enter per unt rate : "))
fixed_charge = int(input("Enter fixed charge : "))
available_money = int(input("Enter available money : "))
energy_charge = units_consumed * per_unit_rate
total_bill = energy_charge + fixed_charge
remainder_money = available_money - total_bill  
surcharge = (5/100)*total_bill
is_available_money_above = available_money > total_bill
is_available_money_equal = available_money == total_bill
print("total_bill = " , total_bill)
print("remainder money = " , remainder_money)
print("are available money above total bill ? " , is_available_money_above)
print("are available money equal total bill ? " , is_available_money_equal)
