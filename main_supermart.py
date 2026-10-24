# Custom module ko import karna (Ch 10)
import inventory_data

print("==========================================")
print("   WELCOME TO SUPERMART SMART BILLING     ")
print("==========================================")

# Available items dikhana
print("\nAvailable Products and Prices:")
for item, details in inventory_data.supermart_inventory.items():
    print(f"- {item.capitalize()} : ₹{details['price']} per unit (Stock: {details['stock']})")

print("\n--- Start Shopping ---")
grand_total = 0
cart = []

while True:
    choice_item = input("\nKharidne ke liye item ka naam daalein (ya bill ke liye 'done' type karein): ").lower()
    
    if choice_item == 'done':
        break
        
    if choice_item in inventory_data.supermart_inventory:
        try:
            qty = int(input(f"Kitni quantity chahiye {choice_item} ki?: "))
            
            # Stock check karna
            if qty <= inventory_data.supermart_inventory[choice_item]["stock"]:
                cost = inventory_data.calculate_item_total(choice_item, qty)
                grand_total += cost
                cart.append((choice_item, qty, cost))
                print(f"Added! {qty}x {choice_item} = ₹{cost}")
            else:
                print("Sorry! Stock me utna item available nahi hai.")
        except ValueError:
            print("Kripya valid number enter karein!")
    else:
        print("Yeh item hamare store me available nahi hai. Dobara try karein.")

# Final Bill Generation
print("\n==========================================")
print("             FINAL BILL SUMMARY           ")
print("==========================================")
for item, qty, cost in cart:
    print(f"{item.capitalize()} (Qty: {qty}) -> ₹{cost}")

print("------------------------------------------")
print(f"GRAND TOTAL: ₹{grand_total}")
print("Thank you for shopping at SuperMart!")
print("==========================================")

