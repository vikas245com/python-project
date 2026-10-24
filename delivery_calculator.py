cart_amount = float(input("Enter your shopping amount: "))
if cart_amount < 500:
   shipping_charge = 50
else:
   shipping_charge = 0
final_cart_amount = cart_amount + shipping_charge
membership = input("you have a primimum membership (yes/no) : ").lower()
discount = 0
if membership == "yes":
   discount = final_cart_amount*0.10
festival_promo_code = input("kya aapke pass festival promo code hai (yes/no): ").lower()
flat = 0
if festival_promo_code == "yes":
   flat = 50
final_amount = final_cart_amount - discount - flat
print(f"cart_amount : {cart_amount}")
print(f"shipping charge : { shipping_charge}")
print(f"discount : {discount}")
print(f"final payable amount : {final_amount}") 

