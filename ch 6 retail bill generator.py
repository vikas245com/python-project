# part 1 : name safai
def clean_name(name):
    return name.strip().title()
# part 2: invoice id padding
def format_bill_no(bill_id):
    return "INV-" + str(bill_id).zfill(5)
# part 3: row trucate aur align karna
def format_item_row(item_name, qty , price):
    # truncation logic
    if len(item_name) > 12:
        display_name = item_name[:12] + "..."
    else:
        display_name = item_name
    # alognment:item left(16), qty center(6), price right(10)
    return f"{display_name:<16}{qty:^6}{price:>10.2f}"

# test run karke single row check karte hain:
print("=" * 35)
print(f"customer : {clean_name('    vikas pareek   ')}")
print(f"bill no   : {format_bill_no(7)}")
print("-" * 35)
print(f"{'item':<16}{'qty':^6}{'price':>10}")
print("-" * 35)
print(format_item_row("Mechanical keyboard" , 1 , 1499.0))
print(format_item_row("Mouse" , 2 , 450.5))
print("=" * 35) 

