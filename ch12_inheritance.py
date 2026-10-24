# 1. Parent Class (Base Class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, mera naam {self.name} hai aur meri umar {self.age} saal hai.")

# 2. Child Class (Derived Class) - Yeh Person se inherit kar rahi hai
class Student(Person):
    def study(self):
        print(f"{self.name} abhi padhai kar raha hai.")

# Object banana (Child class ka object Parent ke methods bhi use kar sakta hai!)
s1 = Student("Vikas", 28)

# Parent class ka method call karna
s1.introduce() 
# Output: Hello, mera naam Vikas hai aur meri umar 28 saal hai.

# Apna khud ka Child class ka method call karna
s1.study() 
# Output: Vikas abhi padhai kar raha hai.

class Animal:
    def breathe(self):
        print("Saans le raha hai...")

class Dog(Animal):
    def bark(self):
        print("Bhonk raha hai: Bhau Bhau!")

d = Dog()
d.breathe() # Parent ka method
d.bark()    # Apna method


class Grandfather:
    def house(self):
        print("Dada ji ka bada ghar hai.")

class Father(Grandfather):
    def car(self):
        print("Papa ki gaadi hai.")

class Son(Father):
    def laptop(self):
        print("Beta apna laptop use kar raha hai.")

s = Son()
s.house() # Dada ji wala method
s.car()   # Papa wala method
s.laptop()# Apna method


class Father:
    def skills_father(self):
        print("Business skills")

class Mother:
    def skills_mother(self):
        print("Art and Cooking skills")

class Child(Father, Mother):
    def skills_child(self):
        print("Coding skills")

c = Child()
c.skills_father() # Papa se mila
c.skills_mother() # Mummy se mila
c.skills_child()  #Khud ka hai

class Vehicle:
    def start(self):
        print("Vehicle start ho gaya.")

class Car(Vehicle):
    def drive_car(self):
        print("Car chal rahi hai.")

class Bike(Vehicle):
    def ride_bike(self):
        print("Bike chal rahi hai.")

  # 1. Parent Class
class Animal:
    def make_sound(self):
        print("Animal kuch aawaz nikal raha hai.")

# 2. Child Class jo Animal se inherit kar rahi hai
class Dog(Animal):
    # Humne parent wale method ka naam hi yahan dobara likh diya (Override kar diya)
    def make_sound(self):
        print("Dog bhonk raha hai: Bhau Bhau!")

# Object banana
d = Dog()

# Jab hum method call karenge, toh kiska chalega? Parent ka ya Dog ka?
d.make_sound() 
# Output: Dog bhonk raha hai: Bhau Bhau!      

# 1. Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 2. Child Class
class Student(Person):
    def __init__(self, name, age, student_id):
        # super() ke zariye humne Parent (Person) ke __init__ ko bula liya
        # taaki name aur age wahi set ho jayein, humein dubara code na likhna pade!
        super().__init__(name, age)
        
        # Yeh student ka apna naya attribute hai
        self.student_id = student_id

# Object banana
s1 = Student("Vikas", 28, "ST101")

print(s1.name)      # Output: Vikas (Parent se mila)
print(s1.age)       # Output: 28 (Parent se mila)
print(s1.student_id)# Output: ST101 (Apna hai)

from abc import ABC, abstractmethod

# 1. Abstract Base Class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Yeh ek rule hai jo child class ko follow karna hi padega"""
        pass

# 2. Child Class jo Shape se inherit kar rahi hai
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Agar hum yahan 'area' method nahi banate, toh Python error dega!
    def area(self):
        return self.length * self.width

# Aagar aap Shape ka direct object banane ki koshish karoge, toh error aayega:
# s = Shape() -> Error! (Aap abstract class ka object nahi bana sakte)

# Lekin Rectangle ka object bilkul ban sakta hai:
rect = Rectangle(10, 5)
print("Rectangle ka Area:", rect.area()) # Output: 50

class Student:
    def __init__(self, name, age, password):
        self.name = name          # 1. Public
        self._age = age           # 2. Protected (ek underscore)
        self.__password = password # 3. Private (do underscore)

# Object banana
s1 = Student("Vikas", 28, "secret123")

# 1. Public variable ko kahin se bhi access kar sakte hain:
print(s1.name)  # Output: Vikas (Asani se chal gaya)

# 2. Protected variable ko bahar se access kar sakte hain (lekin achi habit nahi maani jati):
print(s1._age)  # Output: 28 (Chal jayega, par warning hoti hai)

# 3. Private variable ko bahar se direct access KARNE PAR ERROR AAYEGA:
# print(s1.__password) # Error! Yeh bahar se nahi dikhega.

from typing import final

# 1. Final Class banana
@final
class DatabaseConnection:
    def connect(self):
        print("Database se connection establish ho gaya hai.")

# 2. Agar koi is class se inherit karne ki koshish karega, 
# toh Python ke type checkers (jaise VS Code / Mypy) error denge:

# class HackerConnection(DatabaseConnection): # Yeh error dega!
#     pass

class A:
    def show(self):
        print("Class A ka method")

class B(A):
    def show(self):
        print("Class B ka method")

class C(A):
    def show(self):
        print("Class C ka method")

# Multiple Inheritance: D ne B aur C dono se inherit kiya
class D(B, C):
    pass

# Object banana
d = D()
d.show() 
# Output: Class B ka method (Kyunki D ki bracket mein B pehle likha hai!)
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# 1. Pehli Class (Engine)
class Engine:
    def start(self):
        print("Engine start ho gaya! Vroom Vroom...")

# 2. Doosri Class (Car) jiske andar Engine ka object hoga (Composition)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # Yahan humne Engine class ka object Car ke andar bana diya (Containership)
        self.engine = Engine()

    def start_car(self):
        print(f"{self.brand} {self.model} ko chalu kar rahe hain...")
        # Car apne engine ke method ko call kar rahi hai
        self.engine.start()

# Object banana
my_car = Car("Tesla", "Model S")
my_car.start_car()




