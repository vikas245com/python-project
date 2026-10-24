import pickle 
def manage_text_file():
    print("--- 1. Text File Operations ---")
    with open("student_info.txt" , "w") as file:
        file.write("Student Name: Vikaas Pareek\n")
        file.write("Course: B.Ed Mathmatics\n")
    print("File ban gayi aur data likh diya gaya. ")

    with open("student_info.txt" , "a") as file:
        file.write("Status; Learning Advanced python & File Handling.\n")
    print("file ban gayi aur data likh diya gaya. ")
    with open ("student_info.txt" , "r") as file:
        print("starting pointer position (tell):",file.tell())
        print("\npehle 20 cgaracters:" , file.read(20))
        print("padhne ke baad pointer positiobn (tell):" , file.tell())
        file.seek(0)
        print("\n poori file seek(0) ke baad dubara read ki gayi :")
        print(file.read())
def manage_binary_pickle():
    print("\n---2. object pickling (Binary Mode) ---")
    student_record = {
        "id" : 101,
        "name" : "vikas",
        "subjects" : ["Maths" , "python" , "physics"],
        "scores" : [92, 88, 95]
    } 

    with open("student_data.pkl" , "wb") as bin_file:
        pickle.dump(student_record, bin_file)
    with open("student_data.pkl" , "rb") as bin_file:
        loaded_data = pickle.load(bin_file)
        print("Binary file se un_pickle kiya hua data:") 
        print(loaded_data)
        print((f"student ka naam: {loaded_data['name']}"))
        print(f"pehla subject: {loaded_data['subjects'][0]}")

if __name__ == "__main__":
    manage_text_file()
    manage_binary_pickle() 
