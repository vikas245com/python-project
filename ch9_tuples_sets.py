point = (10, 20)
print(type(point))
print(f"x:{point[0]}, Y : {point[1]}") 

x , y = point
print(f"unpacked -> x: {x} , y: {y}") 

num1 = (5)
num2 = (5,)
print(type(num1))
print(type(num2))

marks = ( 85, 90, 75, 90, 60, 90)
print("90 kitni baar aaya:" , marks.count(90))
print("75 ka index:" , marks.index(75))

numbers = {1, 2, 2, 3, 4, 4, 4, 5}
print("Set numbers:" , numbers)
raw_ids = [101, 102, 101, 103, 102, 104]
unique_ids = list(set(raw_ids))
print("unique IDs:" , unique_ids)

fruits = {"apple" , "banana"}
fruits.add("orange")
fruits.remove("banana")
print("Fruita set:" , fruits)

python_devs = {"Rahul" , "priya" , "Amit" , "Neha"}
java_devs = {"Amit" , "Neha" , "vikas" , "Rohit"}
all_devs = python_devs | java_devs
print("Sabhi Developers:" , all_devs)
both_devs = python_devs & java_devs
print("Dono jante hain:" , both_devs)
only_python = python_devs - java_devs
print("Sirf python Developers:" , only_python)






