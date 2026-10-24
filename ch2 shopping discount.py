product_price = int(input("Enter your product price : "))
discount_percentage = int(input("Enter your discount percentage : "))
discount_amount = (discount_percentage/100)*product_price
print("discount_amount = " , discount_amount )
final_price = product_price - discount_amount 
print("final price = " , final_price ) 
money = int(input("Enter your avaliable money : "))
is_above_1000 = money > 1000 
print("Do you have more than 1000? " , is_above_1000) 
