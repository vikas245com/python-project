customer_name = input("Enter customer name : ")
total_shopping_amount = float(input("Enter shopping amount : "))
available_money = float(input("Enter available money : "))
# discount money rules 
if total_shopping_amount > 10000:
    discount_percentage = 20
elif  total_shopping_amount >= 5000:
    discount_percentage = 10
elif total_shopping_amount  >= 2000:
    discount_percentage =5
else:
   discount_percentage = 0   
discount_amount = (discount_percentage/100)*total_shopping_amount
final_amount = total_shopping_amount - discount_amount 
remaining_money = available_money - final_amount 
if available_money > final_amount:
    print("payment possible")
else:
    print("Insufficient Balance")  
print("final amount : " , final_amount)
print("remaining money : " , remaining_money) 

