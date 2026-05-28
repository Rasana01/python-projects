def main():
    while True:
        print("\n1. Add task")
        print("\n2.View task")
        print("\n3.Remove task")
        print("\n4.Quit")
        choice = input("choose: ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            break
        else:
            print("invalid choice!") 

def add_task():
    task = input("Ehter task: ").strip()
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print(f"task '{task}' added!")
def view_task():
     try:
         with open("tasks.txt", "r")as f:
            tasks = f.readlines() 
            if tasks:
                print("\n Your tasks: ")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                    print("No tasks yet!")
     except FileNotFoundError:
         print("No tasks yet!")                                

def remove_task():
    view_task()
    try:
        n = int(input("Enter task number to remove: "))
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        tasks.pop(n - 1)
        with open("tasks.txt", "w") as f:
            f.writelines(tasks)
        print("Task removed!")
    except (ValueError, IndexError):
        print("Invalid number!")

main()                           