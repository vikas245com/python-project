def format_student_name(raw_name):
    return raw_name.strip().title()
def format_roll_no(roll_num):
    return "Roll - " + str(roll_num).zfill(4)
def format_subject_row(subject,marks):
    if len(subject)>10:
        display_name = subject[:10] + "..."
    else:
        display_name = subject
    
    return f"{display_name:<14}{marks:>6.1f}"

print("=" * 23)
print("      Report Card      ")
print("=" * 23)
print(f"Roll No: {format_roll_no(  24  )}")
print(f"student: {format_student_name('Rahul sharma')}")
print("-"*23)
print(f"{'subject':<14}{'Marks':<6}")
print("-"*23)
print(format_subject_row("mathematics" , 95.5))
print(format_subject_row("English" , 88.0))
print(format_subject_row("computer science" , 99.0))
print("="* 23)
