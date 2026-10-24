class Student:
    school_name  = "Greenwood High"

student1 = Student()
student2 = Student()

print(student1.school_name)
print(student2.school_name) 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_info(self):
        print(f"Hello, mera naam {self.name} hai aur mera marks {self.marks} hain ")

student1 = Student("vikas" , 85)
student2 = Student("Rahul" , 92)
student1.display_info()
student2.display_info()

class Student:
    # Yeh ek Class / Static Variable hai (Sabhi objects ke liye common)
    school_name = "Greenwood High"
    total_students = 0

    def __init__(self, name):
        self.name = name # Instance Variable
        # Jab bhi naya student banega, class variable ki value 1 badh jayegi
        Student.total_students += 1

# Objects banana
s1 = Student("Vikas")
s2 = Student("Rahul")

# Access karna
print(s1.school_name) # Output: Greenwood High
print(s2.school_name) # Output: Greenwood High

# Yeh class member batata hai ki abhi tak kitne total objects ban chuke hain
print("Total Students:", Student.total_students) # Output: 2

class Student:
    school_name = "Greenwood High"

    def __init__(self, name):
        self.name = name

    # Yeh ek Static Method hai
    @staticmethod
    def is_valid_age(age):
        """Check karta hai ki age valid hai ya nahi (18 se kam ya zyada)"""
        if age >= 18:
             return "Adult student"
        else:
             return "Minor student"

# Static method ko aap direct class ke naam se call kar sakte hain bina object banaye!
print(Student.is_valid_age(20)) # Output: Adult student

# Aap object ke through bhi call kar sakte hain
s1 = Student("Vikas")
print(s1.is_valid_age(15)) # Output: Minor student


class Student:
    def __init__(self, name, marks):
        # Yeh instance attributes hain
        self.name = name
        self.marks = marks

    # Yeh ek Instance Method hai kyunki yeh 'self' (object) ka data use kar raha hai
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"{self.name} ke naye marks update ho kar {self.marks} ho gaye hain.")

# Object banana
s1 = Student("Vikas", 85)

# Instance method ko call karna
s1.update_marks(95)
# Output: Vikas ke naye marks update ho kar 95 ho gaye hain.




