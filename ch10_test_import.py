from calculator import add 
print(add(45,65))

import sys

print("Python kahan-kahan modules dhoondhta hai (sys.path):\n")
for path in sys.path:
    print(path)

import builtins

# Dekhte hain ki builtins module ke andar kitni saari cheezein hain
print("Total built-in items:", dir(builtins))

# Hum builtins ko explicit use karke bhi function chala sakte hain:
builtins.print("Hello from builtins module!")

