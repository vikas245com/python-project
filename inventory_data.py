"""
Yeh SuperMart ka Inventory aur Billing module hai.
Yeh stock management aur total price calculation handle karta hai.
"""

# Apne banaye huye calculator module ko import karte hain (Ch 10)
import calculator

# SuperMart ka Inventory Database (Dictionaries - Ch 8)
supermart_inventory = {
    "apple": {"price": 100, "stock": 50},
    "banana": {"price": 40, "stock": 100},
    "milk": {"price": 60, "stock": 30},
    "bread": {"price": 35, "stock": 20}
}

# Unique categories ya customer tracking ke liye Sets (Ch 9)
store_categories = {"Fruits", "Dairy", "Bakery"}

def calculate_item_total(item_name, quantity):
    """Item ke naam aur quantity ke hisaab se total cost calculate karta hai calculator module use karke."""
    if item_name in supermart_inventory:
        price_per_unit = supermart_inventory[item_name]["price"]
        # calculator module ka multiply function use kar rahe hain
        total = calculator.multiply(price_per_unit, quantity)
        return total
    else:
        return None

# Direct Execution Testing Block (Ch 10)
if __name__ == "__main__":
    print("--- inventory_data.py module testing ---")
    print("Module Docstring:", __doc__)
    print("Test calculation for 3 apples:", calculate_item_total("apple", 3))
    