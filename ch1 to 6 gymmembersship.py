def clean_member_name(raw_name):
    return raw_name .strip().title()
def generate_member_id(mem_num):
    return "MEM-"+str(mem_num).zfill(4)
print(clean_member_name("rohit sharma"))
print(generate_member_id(12))

def calculate_gym_fee(plan_type,months):
    if plan_type == "Basic":
        monthly_fee = 500
    elif plan_type == "pro":
        monthly_fee = 1000
    elif plan_type == "vip":
        monthly_fee = 1500
    else:
        monthly_fee = 500
    
    base_amount = monthly_fee * months
    tax = base_amount * 0.18
    total_payable = base_amount + tax 
    return base_amount, tax, total_payable
    
base, tax , total = calculate_gym_fee("pro" ,3)
print(f"base: {base}, tax : {tax} total : {total}")

def print_gym_receipt(mem_id, name, plan, months, base, tax, total):
    print("=" * 34)
    print(f"{'FITNESS CLUB RECEIPT':^34}")
    print(f"Member ID :  {mem_id}")
    print(f"Name      :   {name}")
    print(f"plan      :  {plan}")
    print(f"Duration  : {months} months")
    print("-" * 34)
    print(f"{'Description':<20}{'Amount':>14}")
    print(f"{'Base Membership':<20}{base:>14.2f}")
    print(f"{'GST(18%)':<20}{tax:>14.2f}")
    print(f"{'Total Payable':<20}{total:>14.2f}")
    print("="*34)


member_counter = 1 
while True:
    print("\n===FITNESS CLUB PORTAL ===")
    print("1. New miember Registration")
    print("2. Exit")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        raw_name = input("Enter member name: ")
        plan = input("Enter plan (Basic/pro/vip): ")
        months = int(input("Enter months (e.g. 1, 3, 6,12 "))
        
        name = clean_member_name(raw_name)
        mem_id = generate_member_id(member_counter)
        base, tax, total = calculate_gym_fee(plan, months)
        print_gym_receipt(mem_id, name, plan.upper(), months,base, tax, total)
        member_counter += 1

    elif choice == "2":
        print("Thank you ! exiting portal.")
        break
    else:
        print("Invalid choice, please enter 1 or 2!")
