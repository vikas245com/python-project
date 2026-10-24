item_name = input("Aapko kya kharidna hai (coffee/burger/pizza): ").lower()

# User ki choice ke hisab se base price set karo
if item_name == "coffee":
    item_price = 100
elif item_name == "burger":
    item_price = 150
else:
    item_price = 200

size = input("Aapko kya size chahiye (regular/large): ").lower()
if size == "large":
    item_price = item_price + 50

delivery_option = input("Kya aapko home delivery chahiye (yes/no): ").lower()
if delivery_option == "yes":
    item_price = item_price + 30

discount_code = input("Kya aapke paas discount code hai (yes/no): ").lower()
discount = 0

if discount_code == "yes":
    discount = item_price * 0.10

total_price = item_price - discount
print("Total price : ", total_price)

