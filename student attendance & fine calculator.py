absent_count = 0
total_fine = 0

for i in range(1, 6):
    status = input(f"Student {i} present hai ya absent? (P/A ya stop): ")

    if status == "stop":
        print("Attendance process stopped midway!")
        break

    if status == "P":
        print("Marked Present")
        continue
    elif status == "A":
        absent_count += 1
        total_fine += 50
        print("Marked Absent (Fine: ₹50)")
    else:
        print("Invalid input! Please enter P, A, or stop.")
print("-" * 35)
print("--- Final Attendance Summary ---")
print(f"Total Absent Students : {absent_count}")
print(f"Total Fine Collected  : ₹{total_fine}")
print("-" * 35)