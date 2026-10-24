import math
import random
print("---1. Built in modules ka Upyog ---")
print("pi ki value:" , math.pi)
print("random lucky number (1 se 10 mein):" , random.randint(1,10))
import toolkit  as tk
print("\n--- 2. custom module with Aliasing (tk) ---")
print("5 ka square:" , tk.square(5))
print("3 ka square:" , tk.square(3)) 
print(tk.greet_user("vikas"))
from toolkit import cube 
print("\n--- 3. specific function Import ---")
print("4 ka cube:" , cube(4))

