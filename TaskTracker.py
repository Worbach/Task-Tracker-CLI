"""
To-Do List CLI tool
This CLI tool allows users to do the following:
1. Add tasks
2. Mark tasks complete
3. Un-mark tasks
4. View current tasks
5. View completed tasks
6. Quit
"""

current_tasks = []
completed_tasks = []

def add_task():
    task = input("Enter a new task: ").lower()
    current_tasks.append(task)
    print(f"'{task}' added successfully")

def mark_task_complete():
    if len(current_tasks) == 0:
        print("No tasks found.")
    else:
        print()
        print("Tasks to be completed:")
        for i, t in enumerate(current_tasks):
            print(f"{i + 1}. {t}")
        task = input("Which task did you complete?: ").lower()
        if task in current_tasks:
            print(f"'{task}' completed")
            completed_tasks.append(task)
            current_tasks.remove(task)
        else:
            print("task not found.")

def unmark_task_complete():
    if len(completed_tasks) == 0:
        print("No completed tasks found.")
    else:
        print()
        print("Tasks marked for completion:")
        for i, t in enumerate(completed_tasks):
            print(f"{i + 1}. {t}")
    task = input("Unmark which completed task?: ").lower()
    if task in completed_tasks:
        completed_tasks.remove(task)
        current_tasks.append(task)
        print(f"'{task}' unmarked from completion.")
    else:
        print(f"'{task}' does not exist.")

def view_current_tasks():
    if len(current_tasks) == 0:
        print("No tasks found.")
    else:
        print()
        print("Current Tasks:")
        print()
        for i, task in enumerate(current_tasks):
            print(f"{i + 1}. {task}")
        print()
        print("End of current tasks.")

def view_completed_tasks():
    if len(completed_tasks) == 0:
        print("No tasks found.")
    else:
        print()
        print("Completed Tasks:")
        print()
        for i, task in enumerate(completed_tasks):
            print(f"{i + 1}. {task}")
        print()
        print("End of completed tasks.")

def main():
    # Run the command-line to-do list application.
    while True:
        print()
        print("\n====== To-Do-List CLI tool ======")
        print("1. Add task")
        print("2. Mark task complete")
        print("3. Un-mark task complete")
        print("4. View current tasks")
        print("5. View completed tasks")
        print("6. Quit")

        choice = int(input("Enter a number corresponding to your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            mark_task_complete()
        elif choice == 3:
            unmark_task_complete()
        elif choice == 4:
            view_current_tasks()
        elif choice == 5:
            view_completed_tasks()
        elif choice == 6:
            print("Thank you for using the To-Do-List CLI tool")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

