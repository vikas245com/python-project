print("--- student result manager ---")
student = []
while True:
    print("1. Add Student: ")
    print("2, View All Student: ")
    print("3. Show Class Average: ")
    print("4. Exit ")
    num = input("please select a number given: ")
    if num == "1":
        name = input("Enter student Name: ")
        sub1 , sub2 , sub3 , = map(float, input("Enter your three subject marks with space: ").split())
        if (0 <= sub1 <= 100) and (0 <= sub2 <= 100) and (0 <= sub3 <= 100):
            student_data = {
                "Name" : name,
                "First subject marks" : sub1, 
                "Second subject marks" : sub2,
                "third subject marks" : sub3
            }
            student.append(student_data)
            print("Student added successfully!")
        else:
            print("Error: Marks 0 aur 100 ke beech hi hone chahiye!")
    elif num == "2":
        if not student:
            print("no student data added")
        else:
            for data in student:
                print(data)
    elif num == "3":
        if not student:
            print("No student data added yet!")
        else:
            class_total = 0
            for data in student:
                student_total = data["First subject marks"]+ data ["Second subject marks"] + data ["third subject marks"]
                class_total += student_total
            class_avg = class_total/len(student)
            print(f"Class Average:  {class_avg}")
    elif num == "4":
        print("program band ho raha hai : ")
        break 
    else:
        print("Only 1 se 4 tak number hee add kare! ")
