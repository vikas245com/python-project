valid_categories = ("Grocery" , "Electronics" , "Stationery")
inventory = {
    101:{
        "Name" : "Basmati Rice",
        "price" : 120.0,
        "stock" : 50,
        "category" : "Grocery"
    }
}

active_categories = {"Grocery"} 
print("superMart Inventory System Initialized!")
print("Initial Inventory:", inventory)  

def add_product(inventory_db,valid_cats, active_cats, product_id, name, price, stock, category):
    if product_id in inventory_db:
        print(f"Error: product ID {product_id} pehle se maujood hai!")
        return
    if category not in valid_cats:
        print(f"Error: Invalid category! Allowed categories hain : {valid_cats}")
        return
    inventory_db[product_id] = {
        "Name" : name,
        "price" : price,
        "stock" : stock,
        "category" : category
        
    }

    active_cats.add(category) 
    print(f"Success: Product '{name}' successfully add ho gaya!")

add_product(inventory, valid_categories, active_categories , 102, "wireless Mouse" , 450.0 , 25, "Electronics")
add_product(inventory, valid_categories , active_categories ,103, "Notebook" , 50.0, 100, "Books")
print("\nupdated Inventory:" , inventory)
print("Active Categories Set:" , active_categories)

def view_inventory(inventory_db):
    if len(inventory_db) == 0:
        print("Inventor abhi khaali hai!")
        return
    print("\n--- CURRENT SUPERMART INVENTORY --- ")
    for prod_id, details in inventory_db.items():
        print(f"ID: {prod_id} | Name: {details['Name']} | price: Rs. {details['price']} | stock: {details['stock']} | category: {details ['category']}")


view_inventory(inventory) 

def search_product(inventory_db, product_id):
    if product_id in inventory_db:
        details = inventory_db[product_id]
        print(f"\nProduct Mil Gaya! ID: {product_id}")
        print(f"Name: {details['Name']} | price: Rs. {details['price']} | stock: {details['stock']} | category: {details['category']}")
    else:
        print(f"\nError: Product ID {product_id} inventory mein nahi mila!")

search_product(inventory, 102)
search_product(inventory, 999) 


