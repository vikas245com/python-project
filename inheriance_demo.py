class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary , department):
        super().__init__(name, emp_id, salary)
        self.department = department
    def display_info(self):
        super().display_info()
        print(f"department> {self.department}")
        print("="*30)

print("---Normal Employee Details---")
emp1 = Employee("vikas" , 101, 40000)
emp1.display_info()
print("="*30)

print("--Manager Details (Inherited from Employee) ---")
mgr1 = Manager("Amit" , 102, 80000, "IT Department")
mgr1.display_info()

