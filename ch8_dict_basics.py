product = {
    "name" : "laptop",
    "price": 45000,
    "brand" : "Dell"
}
print(product) 
print(product["brand"]) 
product["ram"] = "16gb"
product["price"] = 42000 
print(product) 

warranty = product.get("warranty" , "Not Available")
print(warranty) 
product.pop("brand")
print(product) 
for k, v in product.items():
    print(f"{k.title()} -> {v}") 


cart = [
    {"name": "Milk", "price": 30.0, "qty": 2},
    {"name": "Bread", "price": 40.0, "qty": 1}
]

inventory = [
    {"name" : "mouse" ,"price" : 500 , "stock" : 10} ,
    {"name" : "keyboard" , "price" : 1200 , "stock" : 5}
]

inventory.append({"name" : "moniter" , "price" : 8500 , "stock" : 5})
print(inventory) 

for item in inventory:
    print(f"product : {item['name']} |, price : Rs. {item ['price']} | stock : {item['stock']}")

for item in inventory:
    if item["name"].lower() == "mouse":
        item["stock"] -= 2
        print(f"mouse ka naya stock: {item['stock']}")
        break
total_val = 0.0
for item in inventory:
    total_val += item["price"]*item["stock"]
print(f"Total inventory value : Rs. {total_val}")

students_db = {
    101: {
        "name": "Rahul Sharma",
        "city": "Jaipur",
        "marks": {"math": 85, "python": 92}
    }
}
print(students_db) 

users = {
    "vikas" : {
        "name" : "vikas",
        "role" : "Admimn" ,
        "active" : True
    }
} 
print(users["vikas"]["role"])

users["vikas"]["role"] = "SuperAdmin"

users["vikas"]["email"] = "vikas@example.com"

users["rahul"] = {
    "name": "Rahul",
    "role": "Editor",
    "active": False
}
for username, details in users.items():
    print(f"username: {username} | Name: {details['name']} | Role: {details['role']}")

users["vikas"].update({"role" : "owner" , "city" : "Jaipur"})
users["rahul"].setdefault("status" , "Active")

print(users["vikas"])
print(users["rahul"])

#{key_expression: value_expression for item in iterable if condition}

prices = {"milk": 30, "bread": 40, "butter": 80}

discounted_prices = {item: price * 0.9 for item, price in prices.items()}
expensive = {item: price for item , price in prices.items() if price > 35}
print(expensive) 
print(discounted_prices) 
squares = {x: x**2 for x in range(1,6)}
print(squares)

















