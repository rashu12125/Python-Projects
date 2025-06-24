def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def todo_list():
    tasks = []
    while True:
        print("\nOptions: add, remove, show, quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "add":
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == "remove":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "show":
            show_tasks(tasks)
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    todo_list()
