# 📝 Personal To-Do List Application
# Author: Aashi Asati
# Hacktoberfest 2025
# Description: CLI-based to-do list app to add, view, and remove tasks

def display_tasks(tasks):
    """
    Display all tasks in a human-friendly format
    """
    if not tasks:
        print("🎉 No tasks in your to-do list!")
        return
    print("\n📋 Your To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    print()  # newline

def add_task(tasks):
    """
    Add a new task to the to-do list
    """
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"✅ Task added: {task}")
    else:
        print("⚠️ Empty task not added!")

def remove_task(tasks):
    """
    Remove a task by its index
    """
    display_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑️ Task removed: {removed}")
        else:
            print("⚠️ Invalid task number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def main():
    tasks = []
    while True:
        print("\n--- Personal To-Do List ---")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Goodbye! Stay productive!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1-4.")

if name == "main":
    main()
