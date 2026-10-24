def add_task(task_list, task_name):
    task_list.append(task_name.strip().title())
    print(f"Task '{task_name.strip().title()}' add ho gaya! ")

def show_tasks(task_list):
    if len(task_list) == 0:
        print("\n koi task nahi hai! list khali hai.")
    else:
        print("\n" + "=" * 25)
        print(f"{'aapke tasks':^25}")
        print("=" * 25)
        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i]}")
        print("=" * 25)

def complete_task(task_list, task_no):
    index = task_no - 1
    if 0 <= index < len(task_list):
        done = task_list.pop(index)
        print(f"badhai ho! '{done}' complete ho gaya aur list se hata diya gaya.")
    else:
        print("galat task number!")

tasks = []
while True:
    print("\n-- TASK MANAGER ---")
    print("1. view Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed (Remove by number )")
    print("4. Exit")
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        show_tasks(tasks)
        if len(tasks) > 0:
            print(f"latest task (aakhri): {tasks[-1]}")
    elif choice == "2":
            new_task = input("Naya task likhein:")
            add_task(tasks,new_task)
    elif choice == "3":
            show_tasks(tasks)
            if len(tasks) > 0:
                t_num = int(input("Kaunsa number complete hua?"))
                complete_task(tasks, t_num)
    elif choice == "4":
            print("task Manager band ho raha hai> shubh din!")
            break
    else:
            print("Galtat option! 1 se 4 tak choose karein. ")


            

