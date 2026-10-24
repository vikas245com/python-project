# my logic
def generate_receipt(customer_name, product , price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount 
    return f" Hello {customer_name}, your order for {product}, is confirmed! final price : Rs. {final_price : 2f}"
receipt = generate_receipt("Rahul" , "wireless Mouse" , 800 , 10)
print(receipt) 

# .format() ke saath
def generate_receipt(customer_name, product, price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return "Hello {}, your order for '{}' is confirmed! Final Price: Rs. {:.2f}".format(customer_name, product, final_price)

# Function ko call kiya aur result store kiya
receipt = generate_receipt("Rahul", "wireless Mouse", 800, 10)
print(receipt)

# f string ke saath 
def generate_receipt(customer_name, product, price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return f"Hello {customer_name}, your order for '{product}' is confirmed! Final Price: Rs. {final_price:.2f}"

# Function ko call kiya aur result store kiya
receipt = generate_receipt("Rahul", "wireless Mouse", 800, 10)
print(receipt)

