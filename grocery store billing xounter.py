total_bill = 0
expensive_items = 0 
for rate in range(1 , 5): 
    price = int(input(f"Enter your item {rate} price: "))
    total_bill += price   
    if price > 100:
        expensive_items += 1        
print("\ntotal bill " , total_bill) 
print(f"100 se mahenge item: {expensive_items} ")
if total_bill > 500:
    print("badhai ho! aapko free delivery milegi!") 