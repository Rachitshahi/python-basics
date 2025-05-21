# -----------------------------
# Simple CLI To-Do List Manager
# -----------------------------

# List to store task dictionaries
todo_list = []

# ---------- CRUD-LIKE OPERATIONS ----------

def add_task(tasks: list) -> None:
    """Add a new task to the to-do list."""
    description = input("Enter task description: ")
    task = {"description": description, "status": "Pending"}
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks: list) -> None:
    """Display all tasks with their statuses."""
    print("\n--- To-Do List ---")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['description']} - {task['status']}")
    else:
        print("No tasks found.")
    print("------------------")

def complete_task(tasks: list) -> None:
    """Mark a task as completed."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Done"
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks: list) -> None:
    """Delete a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted = tasks.pop(task_number - 1)
            print(f"Deleted task: {deleted['description']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# ---------- MAIN MENU LOOP ----------

while True:
    print("\nTo-Do List Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task(todo_list)
    elif choice == '2':
        view_tasks(todo_list)
    elif choice == '3':
        complete_task(todo_list)
    elif choice == '4':
        delete_task(todo_list)
    elif choice == '5':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
