def show_menu():
    print("pizza - 199")
    print("Burger - 99")
    print("coffee - 49")
show_menu() 
def greet_customer(name):
    print(f"namaste {name} ji , aapka swagat hai !")
greet_customer("Rahul")
greet_customer("Amit") 

def calculate_bill(price,quantity):
    total = price*quantity 
    print(f"total bill : {total}") 
calculate_bill(50,3)
calculate_bill(100, 3)     

def add (a,b):
    return a + b 
result = add(10 , 20)
print("result hai :" , result)
final_score = result*2
print("Double score: " , final_score) 

def make_square(num):
    return num * num 
ans = make_square(5) 
print("square hai : " , ans) 

def check_result(marks):
    if marks >= 33:
        return "pass"
    else:
        return "Fail" 
status = check_result(45)
print("student status : " , status )

def get_discount(bill_amount):
    if bill_amount >= 1000:
        return bill_amount * 0.10 
    else:
        return bill_amount * 0
my_discount = get_discount(1500)
final_pay = 1500 - my_discount 
print("my discount : " , my_discount)
print("final pay : " , final_pay) 
          
def calculate(a, b):
    jod = a + b
    ghatav = a - b 
    return jod , ghatav 
sum_ans , diff_ans = calculate(10 , 4)
print("jod: " , sum_ans)
print("ghatav: " , diff_ans)  

def bill_details(price , quantity):
    item_total = price * quantity
    tax_amount = item_total * 0.05
    return item_total , tax_amount 
item_total , tax_amount = bill_details(200,3) 
print("item total : " , item_total)
print("tax amount :" , tax_amount) 


def decorate_name(name):
    print("*" * 20)
    print(f"*   {name}   *")
    print("*" * 20 )
decorate_name("vikas") 

def dynamic_decorated_name(name, symbol="="):
    border = symbol * (len(name) + 6)
    print(border)
    print(f"{symbol}  {name}  {symbol}")
    print(border)

dynamic_decorated_name("vikas")
dynamic_decorated_name("Priya pareek", "*") 

def dynamic_decorated_name(name = "vikas" , role  = "python devloper", symbol = "*"):
    border = symbol * 35 
    print(border)
    print(f"{symbol} name: {name:<25} {symbol}" )
    print(f"{symbol} role: {role:<25} {symbol}")
    print(border) 
dynamic_decorated_name() 
dynamic_decorated_name("Rahul" , "designer" , "=") 

def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # a ban gaya purana b, aur b ban gaya remainder
    return a

# Test karte hain:
result = euclid_gcd(48, 18)
print("GCD / HCF hai:", result)

total_score = 100 
def add_bonus():
    global total_score
    bonus = 50
    total_score += bonus 
    print("Local bonus mila :" , bonus) 
add_bonus()
print("updated global score : " , total_score) 

def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Ab aap chahe 2 number bhejo ya 5, sab chalega!
print(add_all(10, 20))             # Output: 30
print(add_all(5, 10, 15, 20, 25))  # Output: 75

def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Alag-alag detail bhejo:
student_profile(name="Vikas", city="Jaipur", course="Python")

def multiply_all(*args):
    total = 1
    for num in args:
        total *= num  
    return total 
print(multiply_all(2 , 3))
print(multiply_all(2 , 3, 4))  

def print_marksheet(student_name, **subject_marks):
    print(f"--- marksheet of {student_name} ---") 
    total = 0 
    for subject, marks in subject_marks.items():
        print(f"{subject} : {marks}")
        total += marks
    print(f"total marks: {total}")    
print_marksheet("vikas" , math = 85 , science = 90 , english = 78)
   
def countdown(n):
    # 1. Base Case: Rukna kab hai?
    if n == 0:
        print("Khatam!")
        return

    # Kaam: Number print karo
    print(n)

    # 2. Recursive Case: Apne aap ko n - 1 ke sath call karo
    countdown(n - 1)

countdown(3)

def factorial(n):
    # Base case: 1 ka factorial 1 hota hai
    if n == 1:
        return 1
    
    # Apne aap ko call kiya (n - 1) ke sath
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120 

def square(x):
    return x * x

print(square(5))  # Output: 25

square = lambda x: x * x

print(square(5))  # Output: 25

add = lambda a, b: a + b

print(add(10, 20))  # Output: 30

cube = lambda x : x * x * x
print(cube(3))
print(cube(4)) 

numbers = [1, 2, 3, 4]
squared = []

for n in numbers:
    squared.append(n * n)

print(squared)  # Output: [1, 4, 9, 16]

numbers = [1, 2, 3, 4]

# map ne har number ko lambda x: x * x mein pass kiya
squared = list(map(lambda x: x * x, numbers))

print(squared)  # Output: [1, 4, 9, 16]

prices = [100 , 200 , 300, 500]
final_prices = list(map(lambda p: p * 1.18 , prices )) 
print(final_prices) 
print(f"gst ke sath final prices: {final_prices}") 

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Lambda mein 2 arguments liye: a (list1 se) aur b (list2 se)
result = list(map(lambda a, b: a + b, list1, list2))

print(result)  # Output: [11, 22, 33]

prices = [50, 100, 20]
quantities = [2, 3, 5]

total_costs = list(map(lambda p, q: p * q, prices, quantities))

print(total_costs)  # Output: [100, 300, 100]

midterm = [40, 45, 38, 48] 
final_exam = [45, 42, 50, 47] 
total_marks = list(map(lambda m ,f : m + f , midterm , final_exam ))
print(total_marks) 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Sirf wo numbers rakho jinka remainder 2 se divide hone par 0 aaye
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6, 8]

marks = [75, 32, 88, 25, 60, 40]

# Sirf pass wale (33 ya zyada)
passed = list(filter(lambda m: m >= 33, marks))

print(passed)  # Output: [75, 88, 60, 40]

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total_sum = reduce(lambda a, b: a + b, numbers)

print(total_sum)  # Output: 15

from functools import reduce

numbers = [23, 89, 12, 95, 45]

max_num = reduce(lambda a, b: a if a > b else b, numbers)

print(max_num)  # Output: 95

ages = [12, 18, 25, 15, 34, 17, 45, 16]
voters = list(filter(lambda a: a >= 18, ages))
print("Eligible voters:", voters)

from functools import reduce
cart_prices = [450, 120, 999, 230, 50]
total_bill = reduce(lambda a, b: a + b, cart_prices)
print("Total Bill Amount:", total_bill)
