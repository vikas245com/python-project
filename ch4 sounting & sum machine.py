n = int(input("Enter n: "))

total_sum = 0
count = 0

# Pehle saare numbers print karenge aur sath mein sum aur count nikalenge
print("\nNumbers:")
for i in range(1, n + 1):
    print(i)
    total_sum += i  # Har round ka number (i) jud raha hai
    count += 1      # Ginti 1 badh rahi hai

# Loop ke bahar sum aur count print karein
print(f"\nSum = {total_sum}")
print(f"Count = {count}")

# Ab 1 se n tak ke squares print karne ke liye loop
print("\nSquares:")
for i in range(1, n + 1):
    print(i ** 2)   # Har number ka square (i ** 2) print hoga
