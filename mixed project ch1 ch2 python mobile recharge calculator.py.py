customer_name = input("Enter your name : ")
recharge_amount = int(input("Enter your recharge amount : "))
gst_percentage = int(input("Enter your GST percentage : "))
Extra_service_charge = int(input("Enter your extra service charge : ")) 
gst_amount = (gst_percentage*recharge_amount)/100
service_charge = (Extra_service_charge/recharge_amount)*100
final_bill = recharge_amount + gst_amount + Extra_service_charge 
available_money = float(input("Enter available money : "))
is_available_money_above = available_money > final_bill
print("you can afford bill ? " , is_available_money_above)
print("Your final bill is = " , final_bill) 
