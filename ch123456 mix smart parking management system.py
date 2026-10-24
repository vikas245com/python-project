# --- CH 5: FUNCTIONS & CH 6: STRINGS ---
def format_vehicle_no(raw_plate):
    # Cleaning, uppercase, and trimming spaces
    return raw_plate.strip().upper()

def calculate_fee(vehicle_type, hours):
    # --- CH 2: OPERATORS & CH 3: DECISION MAKING ---
    if vehicle_type == "BIKE":
        rate_per_hour = 20
    elif vehicle_type == "CAR":
        rate_per_hour = 50
    elif vehicle_type == "TRUCK":
        rate_per_hour = 100
    else:
        rate_per_hour = 40  # Default rate
    
    total = rate_per_hour * hours
    return total

def print_ticket(ticket_id, vehicle_no, v_type, hours, bill_amount):
    # --- CH 6: STRING FORMATTING, PADDING, ALIGNMENT ---
    padded_id = f"PRK-{str(ticket_id).zfill(4)}"
    
    print("\n" + "=" * 32)
    print(f"{'PARKING RECEIPT':^32}")
    print("=" * 32)
    print(f"Ticket ID : {padded_id}")
    print(f"Vehicle   : {vehicle_no}")
    print("-" * 32)
    print(f"{'Type':<12}{'Hours':^8}{'Amount':>12}")
    print("-" * 32)
    print(f"{v_type:<12}{hours:^8}{bill_amount:>12.2f}")
    print("=" * 32)
    print(f"{'Thank You & Safe Drive!':^32}\n")

# --- CH 4: LOOPING (MAIN PROGRAM) ---
ticket_counter = 1

while True:
    print("=== SMART PARKING SYSTEM ===")
    print("1. Park Vehicle & Generate Bill")
    print("2. Exit System")
    
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == "1":
        # --- CH 1: INPUTS & TYPES ---
        raw_plate = input("Enter Vehicle Number (e.g. rj14-ab-1234): ")
        v_no = format_vehicle_no(raw_plate)
        
        v_type = input("Enter Vehicle Type (Bike/Car/Truck): ").strip().upper()
        hours = int(input("Enter Parked Hours (integer): "))
        
        # Function Calls
        total_bill = calculate_fee(v_type, hours)
        print_ticket(ticket_counter, v_no, v_type, hours, total_bill)
        
        ticket_counter += 1  # Increment for next ticket
        
    elif choice == "2":
        print("Closing System. Goodbye!")
        break
    else:
        print("Invalid choice, please choose 1 or 2.\n")