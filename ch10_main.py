import calculator

result_add = calculator.add(10, 20)
result_mul = calculator.multiply(5, 4)

print("Addition:", result_add)
print("Multiplication:", result_mul)

import calculator

# Module ki docstring access karna
print("Module Documentation:")
print(calculator.__doc__)

# Function ki docstring access karna
print("\nFunction Documentation:")
print(calculator.add.__doc__)

import calculator
import importlib

# 1. Pehli baar import hone par check karna
print("Pehli baar addition:", calculator.add(5, 5))

# 2. Agar hum calculator.py mein code badal dein, 
# toh use dobara load karne ke liye reload use karte hain:
importlib.reload(calculator)

print("Module successfully reload ho gaya hai!")



