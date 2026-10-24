# simple shopping Bill
item1 = input("Enter your first item : ")
price1 = float(input("Enter your first item price : "))
item2 = input("Enter your second item : ")
price2 = float(input("Enter your second item price : "))
sum = price1 + price2 
print("---Simple shoopping Bill---")
print("First item : " , item1 )
print("price : " , price1)
print("second item : " , item2)
print("price : " , price2)
print("="*30)
print(f"{item1}  :   {price1}")
print(f"{item2}  :   {price2}")
print("Total Bill : " , sum) 

