total_steps = 0
target_days = 0
for step in range(1 , 6):
    steps = int(input(f"Enter your day {step} steps :"))
    total_steps += steps
    if steps >= 5000:
        target_days += 1
print("\ntotal steps " , total_steps)
print(f"target poora karne wale din {target_days}")
if target_days >= 3:
    print("shabash! aapne weekly fitness goal achieve kar liya!")
else:
    print(f"agli baar aur mahnat karein! ") 
    