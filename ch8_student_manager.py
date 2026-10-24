students = [] 
def add_student(students_list, roll_no, name, marks):
    for s in students_list:
        if s["roll_no"] == int(roll_no):
            print("yeh roll number pahle se maujood hai!")
            return
    student = {"roll_no" : int(roll_no) , "name" : name.strip().title() , "marks" : float(marks)}
    students_list.append(student)
    print(f"student '{student['name']}' successfully add ho gaya!")
#add_student(students, 101, "rahul sharma", 85)
#add_student(students, 102, "priya verma", 92)

print(students)

def search_student(students_list,roll_no):
    for s in students_list:
        if s["roll_no"] == int(roll_no):
            print(f"\nstudent mil gaya! \nRoll No:{s['roll_no']}\nName:{s['name']}\nMarks:{s['marks']}")
            return
    print("\n yeh roll number nahi mila!")
#search_student(students,101)
#search_student(students, 999) 

def find_topper(students_list):
    if len(students_list) == 0:
        print("koi student data nahi hai!")
        return 
    topper = students_list[0]
    for s in students_list:
        if s["marks"] > topper["marks"]:
            topper = s
    print(f"\nClass Topper: {topper['name']} (Roll No: {topper['roll_no']}) with {topper['marks']} marks!")
#find_topper(students)

while True:
    print("1. Add Student")
    print("2. Search Student by Roll No")
    print("3. Find class Topper")
    print("4. View all students")
    print("5. Exit")

    choice = input("\nEnter choice (1-5):").strip()
    if choice == "1":
        roll = int(input("Roll Number:"))
        name = input("Student Name:")
        marks = float(input("marks: "))
        add_student(students, roll, name, marks)
    
    elif choice == "2":
        roll = int(input("dhoondhne ke liye roll no daalein: "))
        search_student(students, roll)
    elif choice == "3":
        find_topper(students)
    elif choice == "4":
        if len(students) == 0:
            print("Abhi koi student nahi hai!")
        else:
            for s in students:
                print(f"{s['roll_no']} | {s['name']} | Marks: {s['marks']}")
    elif choice == "5":
        print("Program band ho raha hai...")
        break 
    else:
        print("galat choice 1 se t tak chenein.") 








