Employee_name = input("Enter Employee Name : ")
Basic_salary = int(input("Enter Basic salary : ")) 
experience = int(input("Enter your experience(in years) : "))
performance = int(input("Enter your performance score : "))
if experience >= 5 and performance >= 8:
    bonus = 20
elif experience >= 3 and performance >= 6:
    bonus = 10 
else:
    bonus = 5
total_bonus = (bonus/100)*Basic_salary 
final_salary = Basic_salary + total_bonus 
if final_salary >= 50000:
    print("High salary")
elif final_salary >= 30000:
    print("medium salary") 
else:
    print("Entry level")

print("Employee name : " , Employee_name)
print("Basic salary : " , Basic_salary) 
print("experience : " , experience)
print("performance : " , performance)
print("total bonus : " , total_bonus)
print("final salary : " , final_salary)

