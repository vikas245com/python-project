def add_to_cart(items, prices,qtys,name,price,qty):
    clean_name = name.strip().title()
    items.append(clean_name)
    prices.append(float(price))
    qtys.append(int(qty))
    print(f" '{clean_name}' cart mein add ho gaya!")
cart_items = []
cart_prices = []
cart_qtys = []

#add_to_cart(cart_items, cart_prices, cart_qtys, "amul milk  " , 30 , 2)
#add_to_cart(cart_items, cart_prices, cart_qtys, "bread" ,40 , 1)
#print("\nitems list :" , cart_items)
#print("prices list :" , cart_prices)
#print("Qtys list :" , cart_qtys)

def remove_from_cart(items,prices, qtys,item_no):
    index = item_no - 1
    if 0 <= index < len(items):
        r_item = items.pop(index)
        prices.pop(index)
        qtys.pop(index)
        print(f" '{r_item}' ko cart se hata diya gaya hai")
    else:
        print("galat item number!")

#remove_from_cart(cart_items, cart_prices, cart_qtys, 1)
#print("Items bache: " , cart_items)

def calculate_bill(prices,qtys):
    subtotal = 0.0
    for i in range(len(prices)):
        subtotal += prices[i]*qtys[i]
    if subtotal >= 1000:
        discount = subtotal*0.10 
    else:
        discount = 0.0
    texable_amount = subtotal - discount
    gst = texable_amount*0.18
    final_total = texable_amount + gst 

    return subtotal, discount, gst, final_total
#sub , disc, tax, total = calculate_bill(cart_prices, cart_qtys)
#print(f"subtotal: {sub}, discount: {disc}, gst: {tax}, total: {total}")

def print_invoice(items,prices,qtys,subtotal,discount,gst,total):
    print("\n" + "="*42)
    print(f"{'Supermart Invoice' : ^42}")
    print("=" *42)
    print(f"{'item':<16}{'qty':<6}{'price':>8}{'total':>12}")
    print("=" *42)

    for i in range(len(items)):
        line_total = prices[i]*qtys[i]
        print(f"{items[i]:<16}{qtys[i]:<6}{prices[i]:>8.2f}{line_total:>12.2f}")
    print("="*42)
    print(f"{'subtotal' :<26}{subtotal:>16.2f}")
    print(f"{'Discount':<26}{discount:>16.2f}")
    print(f"{'gst(18%)':<26}{gst:>16.2f}")
    print("="*42)
    print(f"{'final payable':<26}{total:>16.2f}")
    print("="*42)
#print_invoice(cart_items, cart_prices, cart_qtys, sub, disc, tax, total)

cart_items = []
cart_prices = []
cart_qtys = []

while True:
    print("\n=== SUPERMART POS SYSTEM ===")
    print("1. Add Item to Cart")
    print("2. Remove Item from Cart")
    print("3. View Cart / Print Bill")
    print("4. Exit")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        name = input("Item ka naam: ")
        price = float(input("Item ki price (Rs): "))
        qty = int(input("Quantity: "))
        add_to_cart(cart_items, cart_prices, cart_qtys, name, price, qty)

    elif choice == "2":
        if len(cart_items) == 0:
            print("Cart pehle se khali hai!")
        else:
            print("\nCart ke items:")
            for i in range(len(cart_items)):
                print(f"{i + 1}. {cart_items[i]}")
            item_no = int(input("Kaunsa number hatana hai? "))
            remove_from_cart(cart_items, cart_prices, cart_qtys, item_no)

    elif choice == "3":
        if len(cart_items) == 0:
            print("Cart khali hai, pehle item add kijiye!")
        else:
            subtotal, discount, gst, total = calculate_bill(cart_prices, cart_qtys)
            print_invoice(cart_items, cart_prices, cart_qtys, subtotal, discount, gst, total)

    elif choice == "4":
        print("System band ho raha hai. Shubh din!")
        break

    else:
        print("Galat choice! 1 se 4 tak choose karein.")

        