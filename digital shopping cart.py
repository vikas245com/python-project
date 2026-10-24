total_bill = 0 
total_items = 0 
while True:
    price = float(input("Enter your product price (0 to stop):")) 
    if price <= 0:
        print("cart closed!")
        break
    total_bill += price
    total_items += 1 

print("-" *30)
print(f"total items purchased : {total_items}")
print(f"grand total bill      :  {total_bill} ") 

