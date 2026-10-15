def get_valid_marks(subject_name):
    while True:
        try:
            marks = float(input(f"Enter {subject_name} marks (0-100)  "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Error marks 0 aur 100 ke beech home chaiye! dobara koshish karein. ")

        except ValueError:
            print("Error: kripya sirf numbers enter karein, text nahi!")        
while True:
    Student_name = input("Enter Student Name: ")
    marks1 = get_valid_marks("first Subject")
    marks2 = get_valid_marks("Second Subject")
    marks3 = get_valid_marks("Third Subject")
    total_marks = marks1 + marks2 + marks3
    maximum_marks = 300 
    percentage = (total_marks/maximum_marks)*100
    print(f"Student Name :  {Student_name}")
    print(f"Total marks :   {total_marks}")
    print(f"percentage:  {percentage:.2f}")

    if marks1 < 33 or marks2 < 33 or marks3 <33:
        print("Result: fail (kyunki kisi subjcet mein marks 33 se kam hain)")
    else:
        if percentage >= 90:
            print("Grade A")
        elif percentage >=75:
            print("Grade B")
        elif percentage >=60:
            print("Grade c")
        elif percentage >=45:
            print("Grade D")
        elif percentage >= 33:
            print("Pass")
        else:
            print("Fail")

    print("="*30)
    choice = input("kya aapko exit karna hai? (1 dabayein exit ke liye, ya Enter dabayein agle student ke liye): ")
    if choice == "1":
        print("Program band ho raha hai. Thank you!")
        break 
