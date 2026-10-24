name = input("Enter your name : ")
age = int(input("Enter your age : "))
education_level = int(input("Enter your education level : "))
python_score = int(input("Enter your python score : "))
sql_score = int(input("Enter your sql score : "))
ml_score = int(input("Enter your ML score : "))
projects_completed = int(input("Enter your projects completed : "))
if age >= 18 and python_score >= 60 and sql_score >= 50:
    print("Basic eligibility :")
if python_score >= 70 and sql_score >= 60 and ml_score >= 60 and projects_completed >= 2:
    print("you are available ai internship eligibility : ")
if python_score >= 80 and sql_score >= 70 and ml_score >= 75 and projects_completed >= 4:
    print("you are advanced candidate : ") 
