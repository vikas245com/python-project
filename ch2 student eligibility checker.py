student_name = input("Enter student name : ")
Age = int(input("Enter your age : "))
marks = int(input("Enter your marks : ")) 
Attendance_percentage = int(input("Enter your attendance percentage : "))  
is_above_age = Age > 18
is_above_marks = marks > 40
is_above_attendance =  Attendance_percentage > 75
print("your age above 18 ? " , is_above_age )
print("your marks above 40 ? " , is_above_marks )
print("your attendance above 75 ? " , is_above_attendance) 
 