class vehicle:
    def __init__(self, brand, modal):
        self.brand = brand
        self.modal = modal

    def display_info(self):
        print(f"brand: {self.brand}")
        print(f"modal: {self.modal}")

class electriccar(vehicle):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def display_info(self):
        super().display_info()
        print(f"battery size : {self.battery_size}")
        print("="*30)

print("--- Normal Vehical Details ---")
car1 = vehicle("Maruti" ,"brezza" , )
car1.display_info()
print("="*30)
print("---Vehical Datails---")
car1 = electriccar("Tata" ,"Curv" , "80KWH")
car1.display_info() 
print("="*30)


