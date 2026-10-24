def generate_invoice_id(category_code, bill_number):
    cc = category_code.upper()
    bn = str(bill_number).zfill(5) 
    return cc + '-' + bn 
print(generate_invoice_id("inv" , 85))
print(generate_invoice_id("bill" , 9)) 