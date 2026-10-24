class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"car brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"price: {self.price}")
        print("="*30)

    def update_price(self, new_price):
        self.price = new_price
        print(f"Naya price update ho gay ahai : {self.price}")
        print("="*30)
car1 = Car("Hyundai" , "creta", 1500000)
car2 = Car("Tata" , "nexon" , 1200000)
print("--- pehil car ki datails---")
car1.display_details()
print("--- doosri car ki details---")
car2.display_details()
print("---creta ka price update kar rahe hain ---")
car1.update_price(1550000)
print("---updated details---")
car1.display_details()



