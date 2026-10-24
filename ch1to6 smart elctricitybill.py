# -------------------------------------------------------------
# CHAPTER 1 TO 6 MIX PROJECT: UTILITY BILLING SYSTEM
# -------------------------------------------------------------

# --- CH 5: FUNCTIONS & CH 6: STRINGS ---
def clean_consumer_name(name):
    return name.strip().title()

def generate_consumer_id(acc_num):
    return "ACC-" + str(acc_num).zfill(5)

# --- CH 2: OPERATORS & CH 3: DECISION MAKING ---
def calculate_bill(units, c_type):
    fixed_charge = 50.0
    
    if c_type == "COMMERCIAL":
        energy_charge = units * 8.5
    else:  # DOMESTIC
        if units <= 100:
            energy_charge = units * 4.0
        else:
            first_100 = 100 * 4.0
            remaining = (units - 100) * 6.0
            energy_charge = first_100 + remaining

    total_amount = energy_charge + fixed_charge
    return energy_charge, fixed_charge, total_amount

# --- CH 6: ALIGNMENT & FORMATTING ---
def print_receipt(cid, name, c_type, units, energy, fixed, total):
    print("\n" + "=" * 34)
    print(f"{'ELECTRICITY RECEIPT':^34}")
    print("=" * 34)
    print(f"Consumer ID : {cid}")
    print(f"Name        : {name}")
    print(f"Category    : {c_type}")
    print("-" * 34)
    print(f"{'Description':<22}{'Amount':>12}")
    print("-" * 34)
    unit_text = f"Units Consumed ({int(units)})"
    print(f"{unit_text:<22}Rs.{energy:>9.2f}")
    print(f"{'Fixed Meter Charge':<22}Rs.{fixed:>9.2f}")
    print("-" * 34)
    print(f"{'Total Payable':<22}Rs.{total:>9.2f}")
    print("=" * 34)
    print(f"{'Please Pay Before Due Date':^34}")
    print("=" * 34 + "\n")

# --- CH 1: INPUTS & CH 4: LOOPING ---
account_counter = 1

while True:
    print("=== UTILITY BILLING PORTAL ===")
    print("1. Generate Bill")
    print("2. Exit")
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == "1":
        raw_name = input("Enter Consumer Name : ")
        name = clean_consumer_name(raw_name)
        
        c_type = input("Enter Consumer Type (DOMESTIC/COMMERCIAL): ").strip().upper()
        units = float(input("Enter Units Consumed: "))
        
        cid = generate_consumer_id(account_counter)
        energy, fixed, total = calculate_bill(units, c_type)
        
        print_receipt(cid, name, c_type, units, energy, fixed, total)
        account_counter += 1
        
    elif choice == "2":
        print("Exiting program. Have a nice day!")
        break
    else:
        print("Invalid choice, please enter 1 or 2!\n")