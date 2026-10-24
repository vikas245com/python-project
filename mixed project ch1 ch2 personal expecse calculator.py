name = input("Enter your name : ")
MI = int(input("Enter your monthly income ; "))
FE = int(input("Enter your food expense : ")) 
TE = int(input("Enter your travel expense : "))
SE = int(input("Enter your shopping expense : "))
OE = int(input("Endter your other expense : ")) 
TE = FE + TE + SE + OE 
RM = MI - TE 
SP = (RM/MI)*100
print(" Total expecse" , TE)
print("Remaining money" , RM)
print("Saving percentage " , SP )
is_expense = MI > TE 
print("are expenses less than MI ? " , is_expense)