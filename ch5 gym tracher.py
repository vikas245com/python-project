def get_base_fee(months, monthly_rate = 1000):
    total_fee = months * monthly_rate
    return total_fee
#print(get_base_fee(3))
#print(get_base_fee(6 , 800)) 

def calculate_extras(*charges):
    total = 0
    for sum in charges:
        total += sum 
    return total
#print(calculate_extras(500, 300))
#print(calculate_extras())

def get_discount(plan_type , amount):
    if plan_type == "Annual" :
        return amount * 0.20
    elif plan_type == "half-yearly" :
        return amount * 0.10
    else:
        return amount *0
#print(get_discount("Annual" , 5000))
#print(get_discount("Monthly" , 1000)) 

def generate_gym_bill(member_name, months, plan_type , *extras):
    base_amount = get_base_fee(months) 
    extra_amount = calculate_extras(*extras)
    subtotal = base_amount + extra_amount  
    discount_amount = get_discount(plan_type , subtotal)
    final_amount = subtotal - discount_amount 

    print("=" * 30)
    print("      gym membership bill") 
    print("=" * 30)
    print(f"member name : {member_name}")
    print(f"plan type : {plan_type}  ({months} months)")
    print(f"base fee  :  Rs. {base_amount}")
    print(f"Extra fee : {extra_amount}") 
    print(f"subtotal :  {subtotal}")
    print(f" discount : {discount_amount}")
    print("-" * 30)
    print(f"final pay :     Rs. {final_amount}")
    print("=" * 30)
generate_gym_bill("Vikas" , 12, "Annual" , 500, 300) 

 
