import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

# Load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Display the tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()