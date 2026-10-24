def calculate_stay_cost(days, rate_per_day = 200):
    total_rate = days * rate_per_day
    return total_rate
def calculate_room_services(*service_charge):
    total = 0
    for i in service_charge:
        total += i
    return total
def calculate_discount(guest_type , total_amount):
    if guest_type == "vip":
        return total_amount * 0.15
    elif guest_type == "regular" :
        return total_amount * 0.10
    else:
        return total_amount*0
    
def generate_hotal_bill(guest_name , days , guest_type , * service_charge):
        base_cost = calculate_stay_cost(days)
        room_service = calculate_room_services(*service_charge)  
        subtotal = base_cost + room_service
        discount_amount = calculate_discount(guest_type , subtotal)
        final_pay = subtotal - discount_amount
        print("-" * 30)
        print("        hotel Booking Bill  ")
        print("=" * 30)
        print(f"guest name : {guest_name}")
        print(f"days  : {days}")
        print(f"base cost : {base_cost}")
        print(f"services cost : {room_service}") 
        print(f"discount amount : {discount_amount}")
        print("-"*30)
        print(f"Final pay : {final_pay}")
        print("=" * 30)
generate_hotal_bill("Vikas" , 10 , "vip"  , 1000)


