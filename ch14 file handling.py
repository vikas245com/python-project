# 1. File ko Write mode ('w') mein kholna aur kuch likhna
file = open("student.txt", "w")
file.writepehla = file.write("Hello Vikas! Yeh Python se likhi gayi pehli line hai.\n")
file.close()  # Kaam khatam hone par file band karna zaroori hai!

# 2. Usi file ko Read mode ('r') mein kholkar padhna
file = open("student.txt", "r")
content = file.read()
print("File ke andar kya hai:")
print(content)
file.close()


# With statement ka use (Best Practice)
with open("student.txt", "r") as file:
    print(file.read())
# Yahan file apne aap band ho chuki hai!

with open("student.txt", "r") as file:
    line1 = file.readline()
    print("Pehli line:", line1)
    
    line2 = file.readline()
    print("Doosri line:", line2)

with open("student.txt", "r") as file:
    lines_list = file.readlines()
    print("List ka roop:", lines_list)
    print("Kul kitni lines hain:", len(lines_list))

# File ko write mode ('w') mein khola
with open("notes.txt", "w") as file:
    file.write("Pehli line: Hello Vikas!\n")
    file.write("Doosri line: Python file handling sikh rahe hain.\n")

print("Data successfully likha gaya!")

# Kai lines ki ek list
lines_data = [
    "Apple\n",
    "Banana\n",
    "Mango\n"
]

# File ko append mode ('a') mein khola taaki purana data na mite
with open("notes.txt", "a") as file:
    file.writelines(lines_data)

print("Poori list file mein add ho gayi!")

with open("student.txt", "r") as file:
    print("Shuruat mein pointer kahan hai:", file.tell()) # Output: 0 (Pehle byte par)
    
    data = file.read(5) # Pehle 5 characters padhe
    print("5 characters padhne ke baad pointer:", file.tell()) # Output: 5

with open("student.txt", "r") as file:
    # Pehle 5 characters padhe
    print(file.read(5))
    
    # Ab pointer ko wapas file ke shuruat (0th position) par bhej diya!
    file.seek(0)
    
    print("Wapas shuruat se padha:", file.read(5))
with open("source.txt", "w") as f:
    f.write("yeh source file ka data hai. \n")
#ab aapka upar wala code bina error ke chat jayega!

# 1. Ek sath do files kholiin: ek read mode mein, doosri write mode mein
with open("source.txt", "r") as source_file, open("destination.txt", "w") as dest_file:
    
    # Source file ka poora data padha
    data = source_file.read()
    
    # Wo data destination file mein likh diya
    dest_file.write(data)

print("Data successfully source file se destination file mein copy ho gaya!")

# 1. Numbers ko file mein likhna (Convert int to str)
marks = 85
with open("marks.txt", "w") as file:
    # file.write() sirf string leta hai, isliye str() lagana zaroori hai
    file.write(str(marks))

print("Marks successfully file mein save ho gaye!")


# 2. File se number ko wapas padhna aur Math calculation karna
with open("marks.txt", "r") as file:
    data = file.read() # Yeh abhi string hai: "85"
    print("File se aaya data (String format):", type(data))
    
    # Ganit karne ke liye ise integer mein badalna padega!
    actual_marks = int(data)
    
    # Ab hum isme calculation kar sakte hain
    new_marks = actual_marks + 5
    print("5 number bonus milne ke baad total marks:", new_marks)

# 1. Purani image ko read binary ('rb') mein khola, aur nayi ko write binary ('wb') mein
#with open("photo.jpg", "rb") as source_file, open("copy_photo.jpg", "wb") as dest_file:
    
    # Poori image ka data bytes ki form mein read kiya
    #binary_data = source_file.read()
    
    # Wahi raw bytes nayi file mein likh diye
    #dest_file.write(binary_data)

#print("Binary file (Image) successfully copy ho gayi!")


import pickle

# Ek Python Dictionary (Object)
student_info = {
    "name": "Vikas Pareek",
    "course": "B.Ed Mathematics",
    "marks": [85, 90, 92]
}

# 1. Object ko file mein save (dump) karna
with open("student_obj.pkl", "wb") as file:
    pickle.dump(student_info, file)

print("Python object successfully file mein save ho gaya!")


# 2. File se object ko wapas load karna
with open("student_obj.pkl", "rb") as file:
    loaded_object = pickle.load(file)

print("File se wapas aaya data:", loaded_object)
print("Data ka type:", type(loaded_object)) # Output: <class 'dict'>

import dill

# 1. Ek lambda function banaya jo number ka square nikalta hai
square_func = lambda x: x * x

# 2. Dill ka use karke is poore function ko file mein save (dump) kar diya
with open("my_function.pkl", "wb") as file:
    dill.dump(square_func, file)

print("Function successfully dill module se file mein save ho gaya!")


# 3. Ab file se us function ko wapas load karte hain
with open("my_function.pkl", "rb") as file:
    loaded_func = dill.load(file)

# 4. Wapas aaye hue function ko use karke dekhte hain
result = loaded_func(5)
print("File se load kiye gaye function ka output (5 ka square):", result)
# Output: 25






