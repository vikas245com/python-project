name = input("Enter Customer Name : ")
amount = float(input("Enter Shopping amount : "))
discount_percentage = float(input("Enter your discount percentage: "))
discount_amount = (discount_percentage/100)*amount
final_amount = amount - discount_amount
print("---simple shopping Discount Calculator---")
print(f"Customer Name : {name}")
print(f"Shooping amount : {amount}")
print(f"Discount percentage :  {discount_percentage}")
print(f"original Amount:  {amount}")
print(f"discount :  {discount_amount}")
print(f"Final Amount : {final_amount}")


