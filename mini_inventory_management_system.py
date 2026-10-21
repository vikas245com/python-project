print("--- Mini inverntory Management System---")
product_list = []
while True:
    print("1. Add product")
    print("2. view All Products ")
    print("3. Search Product ")
    print("4. Update Product Price ")
    print("5. Show Total Inventory Value ")
    print('6.Exit ')
    choice = input("Plese choose any number given: ")
    if choice == "1":
        product_name = input("Enter your product Name: ").strip()
        product_price = float(input("Enter your product price: "))
        product_quantity = int(input("Enter your product quantity: "))
        product_item = {
            "product name" : product_name,
            "product price" : product_price,
            "product quantity" : product_quantity
        }
        product_list.append(product_item)
        print("your product details added sucessfully added!")
    elif choice == "2":
        if not product_list:
            print("your product store is empty")
        else:
            for item in product_list:
                print(item)
    elif choice == "3":
        if not product_list:
            print("no product added")
        else:
            search_name = input("Enter your product name!").strip()
            found = False
            for item in product_list:
                if item["product name"] == search_name:
                    print(f"product found -> product: {item['product name']}, product price: {item['product price']}, product quantity: {item['product quantity']}")
                    found = True
                    break
            if not found:
                print("your product not found")
    elif choice == "4":
        if not product_list:
            print("No products added yet! ")
        else:
            update_name = input("Enter product name to update price:").strip()
            found = False 
            for item in product_list:
                if item["product name"] == update_name:
                    new_price = float(input("Enter new price:"))
                    item["product price"] = new_price
                    print("Product price updated successfully")
                    found = True
                    break
            if not found:
                print("Product not found!")
    elif choice == "5":
        if not product_list:
            print("No products added yet!")
        else:
            total_inventory_value = 0
            for item in product_list:
                total_value = item['product quantity'] * item['product price']
                total_inventory_value += total_value
            print(f"total inventory value: {total_inventory_value}")
    elif choice == "6":
        print("program band ho raha hai , Exit")
        break
    else:
        print("only 1 se 6 tak hee number hee add karain!")


               
    









    