import json

# ==========================================
# 1. FILE HANDLING FUNCTIONS (Data lana aur save karna)
# ==========================================

def load_data():
    # Yeh function program start hote hi JSON file se purana data nikalega
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Agar file pehli baar mein nahi milti, toh khali list dega
        return []

def save_data(students_list):
    # Yeh function aapke list ke naye data ko JSON file mein save karega
    with open("students.json", "w") as file:
        json.dump(students_list, file, indent=4)


# ==========================================
# 2. CORE FUNCTIONS (Add, View, Search, Update, Delete)
# ==========================================

def add_student(students_list):
    # Naya student add karne ka function
    name = input("Enter student name: ")
    
    # Roll Number Inpur aur Duplicate Check loop
    while True:
        try:
            roll_number = int(input("Enter roll number: "))
            duplicate = False
            for student in students_list:
                if student.get("roll_number") == roll_number:
                    duplicate = True
                    break
            
            if duplicate:
                print("Yeh roll number pehle se majood hai! Koi dusra try karein.")
            else:
                break # Agar duplicate nahi hai toh loop se bahar niklo
        except ValueError:
            print("Kripya sirf valid number enter karein!")

    # Marks Input aur Validation loop (0 se 100)
    while True:
        try:
            marks = float(input("Enter marks: "))
            if 0 <= marks <= 100:
                break # Agar marks sahi hain toh loop se bahar niklo
            else:
                print("Marks sirf 0 se 100 ke beech hone chahiye!")
        except ValueError:
            print("Kripya sirf valid number enter karein!")

    # Teeno cheezein milne ke baad dictionary banakar save karna
    student_dict = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks
    }
    students_list.append(student_dict)
    save_data(students_list)
    print("\nStudent added successfully!")


def view_all_students(students_list):
    # Saare students ko print karne ka function
    print("\n--- All Students Record ---")
    if len(students_list) == 0:
        print("No students found! Pehle kuch students add karein.")
    else:
        for student in students_list:
            print(f"Roll No: {student['roll_number']} | Name: {student['name']} | Marks: {student['marks']}")
            print("-" * 40)


def search_student(students_list):
    # Roll number ke zariye kisi ek student ko dhoondhna
    try:
        search_roll = int(input("Enter roll number to search: "))
        found = False
        
        for student in students_list:
            if student.get("roll_number") == search_roll:
                print("\n--- Student Found ---")
                print(f"Name: {student['name']} | Roll No: {student['roll_number']} | Marks: {student['marks']}")
                found = True
                break
                
        if not found:
            print("Is roll number ka koi student nahi mila!")
    except ValueError:
        print("Invalid input! Kripya sahi roll number enter karein.")


def update_marks(students_list):
    # Puraane student ke marks change karna
    try:
        update_roll = int(input("Enter roll number to update marks: "))
        found = False
        
        for student in students_list:
            if student.get("roll_number") == update_roll:
                while True:
                    try:
                        new_marks = float(input("Enter new marks (0-100): "))
                        if 0 <= new_marks <= 100:
                            student["marks"] = new_marks # Marks update kar diye
                            save_data(students_list)     # File mein naye marks save kar diye
                            print("Marks successfully updated!")
                            found = True
                            break
                        else:
                            print("Marks 0 se 100 ke beech hone chahiye!")
                    except ValueError:
                        print("Kripya valid number enter karein.")
                break 
                
        if not found:
            print("Is roll number ka koi student nahi mila!")
    except ValueError:
        print("Invalid input!")


def delete_student(students_list):
    # Kisi student ka record delete karna
    try:
        delete_roll = int(input("Enter roll number to delete: "))
        
        for i in range(len(students_list)):
            if students_list[i].get("roll_number") == delete_roll:
                del students_list[i] # List se student ko delete kar diya
                save_data(students_list) # File update kar di
                print("Student successfully deleted!")
                return # Delete hone ke baad function yahi khatam
                
        print("Is roll number ka koi student nahi mila!")
    except ValueError:
        print("Invalid input!")


# ==========================================
# 3. MAIN PROGRAM (Yeh loop lagataar chalta rahega)
# ==========================================

# Program shuru hote hi purani file se data le lo
students = load_data()

while True:
    print("\n--- Student Record Manager 2.0 ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_all_students(students)
    elif choice == "3":
        search_student(students)
    elif choice == "4":
        update_marks(students)
    elif choice == "5":
        delete_student(students)
    elif choice == "6":
        print("Exiting Program... Have a great day!")
        break # Break dabte hi program poori tarah band ho jayega
    else:
        print("Invalid choice! Kripya 1 se 6 ke beech ka koi number chunein.")