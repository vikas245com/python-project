cities = ["jaipur" , "delhi" , "mumbai" , "pune"]
print("poori list:" , cities)
print("pehla shehar:", cities[0])
print("aakhri shehar:" , cities[-1])

numbers = [10, 20, 30, 40, 50, 60]
# Index:    0   1   2   3   4   5

# Index 1 se lekar 4 se pehle tak (1, 2, 3)
print(numbers[1:4])   # Output: [20, 30, 40]

# Shuru se lekar index 3 se pehle tak
print(numbers[:3])    # Output: [10, 20, 30]

# Index 3 se lekar aakhir tak
print(numbers[3:])    # Output: [40, 50, 60]

colors = ["Red", "Green", "Blue", "Yellow"]

print(colors[-1])   # Yellow
print(colors[-2])   # Blue

fruits = ["Apple", "Banana", "Mango"]

# Banana (index 1) ki jagah "Orange" rakh do:
fruits[1] = "Orange"

print(fruits)   # Output: ['Apple', 'Orange', 'Mango']

scores = [45, 88, 72, 91, 68, 55]
print(scores[2:5])
print(scores[:-1])
scores[0] = 100 
print(scores) 