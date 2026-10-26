print("--- Student Fee Management System---")
students = []
def add_student():
    name = input("Enter student name:")
    roll_number = int(input("Enter your roll number: "))
    total_fees = int(input("Enter Fees: "))
    student_data = {
                    "name" : name,
                    "roll_number" : roll_number,
                    "total_fees" : total_fees,
                    "paid_fees" : 0 
                    }
    students.append(student_data)
    print("Expense added successfully:")
def pay_fees():
    print("\n--- Pay Fees ---")
    search_roll = int(input("Enter your roll number:"))
    for student in students:
        if student["roll_number"] == search_roll:
            remaining_fees = student["total_fees"]
            if remaining_fees == 0:
                print("Is student ki puri fees pahle hee jama ho chuki hai!")
                return
            print(f"Student Name: {student['name']}")
            print(f"Remaining Fees: {remaining_fees}")
            amount = int(input("Enter amount to pay:"))
            if amount <= 0:
                print("Error: Payment 0 ya negative(minus) nahi ho sakti!")
            elif amount > remaining_fees:
                print(f"Error: aap bachi hui fees ({remaining_fees}) se zyada pay nahi ker sakte!")
            else:
                student["paid_fees"] += amount 
                print(f"Payment successfull ab inki total paid fees {student['paid_fees']} hai.")
                return
    print("Error: ye roll number hamare data mein nahi mila!")
def view_students():
    print("\n--- View All Students ---")
    if not students:
        print("Abhi tak koi student add nahi hua hai:")
        return
    for student in students:
        remaining = student["total_fees"] - student["paid_fees"]
        print(f"Name: {student['name']}, Roll No: {student['roll_number']}, Total fees: {student['total_fees']}, Paid: {student['paid_fees']}, Remaining: {remaining} ")
def search_student():
    print("\n --- Search Student ---")
    search_roll = int(input("Enter student roll number to search: "))
    for student in students:
        if student["roll_number"] == search_roll:
            remaining = student["total_fees"] - student["paid_fees"]
            print("n\--- Student Found ---")
            print(f"Name: {student['name']}")
            print(f"Roll Number: {student['roll_number']}")
            print(f"Total Fees: {student['total_fees']}")
            print(f"Paid Fees: {student['paid_fees']}")
            print(f"Remaining Fees: {remaining}")
            return
    else:
            print("Error: iss roll number ka koi student nahi mila!")

while True:
    print("1. Add Student")
    print("2. Pay Fees")
    print("3. View All Student")
    print("4. Search Student")
    print("5. Exit")
    choice = input("Enter choice number:")
  
    if choice == "1":
        add_student()
    elif choice == "2":
        pay_fees()
    elif choice == "3":
        view_students()
    elif choice == "4":
        search_student()
    elif choice == "5":
        print("Exiting program ...")
        break
    else:
        print("Invalid choice! please enter a number between 1 se 5.  ")
         