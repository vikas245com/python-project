student_name = input("Enter your student name  : ")
hindi = int(input("Enter your Hindi marks : "))
math = int(input("Enter your math marks : "))
social_science = int(input("Enter your social science marks : "))
science = int(input("Enter your science marks : "))
english = int(input("Enter your english marks  : "))
max_marks =500 
total_marks = hindi + math + social_science + science + english 
percentage = (total_marks/max_marks)*100
average_marks = total_marks / 5 
highest_marks = max(hindi , math , social_science , english , science )
is_above_percentage = percentage > 60 
all_subject_marks_above = total_marks > 40 
print("total marks = " , total_marks)
print("percentage = " , percentage)
print("average marks = " , average_marks)
print("are percentage above 60 " , is_above_percentage)
print("are all subject marks above 40 " , all_subject_marks_above) 