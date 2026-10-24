def calculate_subtotal(*prices):
    total = 0
    for price in prices: 
        total += price
    return total
#print(calculate_subtotal(500, 250 , 150)) 

def apply_discount(amount, discount_percent = 10):
    discount_amount = amount*(discount_percent/100)
    return amount - discount_amount 
#print(apply_discount(1000)) 
#print(apply_discount(1000 , discount_percent = 20))

def add_tax(amount, tax_rate = 18):
    tax = amount * (tax_rate /100)
    return amount + tax 
#print(add_tax (900))
#print(add_tax(100 , 5))


def generate_bill(customer_name, *prices, discount=10, tax=18):
    # 1. Purane functions ko call karke values nikali
    subtotal = calculate_subtotal(*prices)
    after_discount = apply_discount(subtotal, discount)
    final_amount = add_tax(after_discount, tax)
    
    # 2. Receipt print ki
    print("=" * 30)
    print("       INVOICE / BILL")
    print("=" * 30)
    print(f"Customer Name : {customer_name}")
    print(f"Items Count   : {len(prices)}")
    print(f"Subtotal      : Rs. {subtotal}")
    print(f"Discount Rate : {discount}%")
    print(f"Tax Rate (GST): {tax}%")
    print("-" * 30)
    print(f"Final Pay     : Rs. {final_amount:.2f}")
    print("=" * 30)

# Function ko call karke test karein:
generate_bill("Vikas", 500, 250, 150)