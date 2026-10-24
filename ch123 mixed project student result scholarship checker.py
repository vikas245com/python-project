student_name = input("Enter student name : ")
age = int(input("Enter you age : "))
family_income = int(input("Enter your family income : "))
marks = list(map(int,input("Enter 5 subject marks (space dekar): ").split())) 
total_marks = sum(marks)
average = total_marks/len(marks)
percentage = (total_marks/500)*100 
if percentage >= 75:
    print("Excellent")
elif percentage >= 60:
    print("Good")
elif percentage >= 40:
    print("pass")
else:
    print("Fail")
if percentage >= 75 and family_income <= 300000:
    print("you are eligibile for scholarship : ")
