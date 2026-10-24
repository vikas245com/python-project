customer_name = input("Enter customer name : ")
unit = int(input("Enter your units consumed : "))
if 0 <= unit <= 100:
    rate = 5
elif 101 <= unit <= 200:
    rate = 7 
elif 201 <= unit <= 300:
    rate = 10
else:
    rate = 15
final_bill = unit * rate 
print("customer name : " , customer_name)
print("units consumed : " , unit)
print("final bill : " , final_bill )

