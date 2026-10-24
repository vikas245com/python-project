#print("Mini Marks calculator")
name = input("Enter your name : ")
marks1 = float(input("Enter your maths marks : "))
marks2 = float(input("Enter your Science marks : "))
marks3 = float(input("Enter your English marks : "))
Total_marks = marks1 + marks2 + marks3 
maximum_marks = 300
percentage = (Total_marks/maximum_marks)*100
percentage = round(percentage, 2)
print("---Mini Marks Calculator---")
print(f"Student Name :  {name}")
print(f"Math marks :   {marks1}")
print(f"Science Marks :  {marks2}")
print(f"English Marks  :  {marks3}")
print(f"Total Marks :  {Total_marks}")
print(f"percentage :  {percentage}") 
