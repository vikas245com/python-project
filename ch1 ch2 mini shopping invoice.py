customer_name = input("Enter your name: ")

# map(int, ...split()) se dono number ek saath integer ban jayenge
p1, q1 = map(int, input("Enter your product 1 price and quantity: ").split())
p2, q2 = map(int, input("Enter your product 2 price and quantity: ").split())
p3, q3 = map(int, input("Enter your product 3 price and quantity: ").split())

discount_percentage = int(input("Enter discount percentage: "))
gst_percentage = int(input("Enter GST percentage: "))
customer_available_money = float(input("Enter available money: "))

# Har item ka kul moolya (Price * Quantity)
item1_cost = p1 * q1
item2_cost = p2 * q2
item3_cost = p3 * q3

subtotal = item1_cost + item2_cost + item3_cost

# Discount calculation
discount_amount = (subtotal * discount_percentage) / 100
amount_after_discount = subtotal - discount_amount

# GST calculation (discount ke baad bachi raqam par)
gst_amount = (amount_after_discount * gst_percentage) / 100

total_bill = amount_after_discount + gst_amount
remaining_money = customer_available_money - total_bill
can_afford = customer_available_money >= total_bill

print("-" * 35)
print("Subtotal (Total Price)  =", subtotal)
print("Total Discount          =", discount_amount)
print("GST Amount              =", gst_amount)
print("Final Bill              =", total_bill)
print("Can customer pay bill?  =", can_afford)
print("Remaining Money         =", remaining_money)