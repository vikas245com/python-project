print("--- Mini To Do List---")
tasks = []
while True:
    print("1. Add Task ")
    print("2. View all task ")
    print("3. Search task")
    print("4. Exit")
    num = input("please select given number!")
    if num  == "1":
        task = input("Enter your task !")
        task_list = {
            "Task name" : task
        }
        tasks.append(task_list)
    elif num == "2":
        if not tasks:
            print("tasks list empty")
        else:
            for item in tasks:
                print(item)
    elif num == "3":
        if not tasks:
            print("no task added")
        else:
            search_name = input("Enter your task!")
            found = False
            for item in tasks:
                if item ["Task name"] == search_name:
                    print(f"task name :  {item['Task name']}")
                    found = True
                    break
            if not found:
                print("your task not found!")
    elif num == "4":
        print("program band ho raha hai !")
        break
    else:
        print("only 1 se 4 tak hee number add kare ")
            