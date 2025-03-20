import os
import json
from datetime import datetime


print("Welcome to the CLI Task Tracker.")
# JSON Functionality
#----------------------------------------------------------------------------------------------------------------------#
TASK_FILE = "tasks.json"

def save_file(tasks):
    """Save tasks to a JSON file."""
    try:
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks file: {e}")

def load_file():
    """Load tasks from a JSON file."""
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading tasks file: {e}")
            return [] # Return an empty list if an error occurs
    return [] # Return an empty list if the file does not exist

tasks = load_file()
#----------------------------------------------------------------------------------------------------------------------#

# Add, Update, and Delete Task Functions
#----------------------------------------------------------------------------------------------------------------------#
def add_task():
    """Adds a new task when user chooses Add"""
    task = input("Enter your new task: ").strip()
    task_id = len(tasks) + 1
    description = input("Enter a description for the new task: ")
    status = int(input("Enter a starting status number for the new task: (1. todo, 2. in-progress, 3. done "))
    createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Current date and time
    updatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Current date and time

    if status == 1:
        status = "todo"
    elif status == 2:
        status = "in progress"
    elif status == 3:
        status = "done"
    else:
        print("Please enter a valid number. (1. todo, 2. in-progress, 3. done)")

    # Append new task to JSON File
    tasks.append({
        "task_id": task_id,
        "task": task,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt
    })
    save_file(tasks) # Save the new task to file

def view_tasks():
    global tasks
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {json.dumps(task, indent=4)}")


def update_task():
    view_tasks()
    task_index = int(input("Enter the number of the task you want to update: ")) - 1
    if 0 <= task_index < len(tasks):
        updated_task = input("Enter the updated task: ").strip()
        updated_description = input("Enter the updated description: ").strip()
        updated_status = int(input("Enter the updated status number: (1. todo, 2. in-progress, 3. done) "))

        if updated_status == 1:
            updated_status = "todo"
        elif updated_status == 2:
            updated_status = "in progress"
        elif updated_status == 3:
            updated_status = "done"
        else:
            print("Please enter a valid number. (1. todo, 2. in-progress, 3. done)")

        tasks[task_index]["task"] = updated_task
        tasks[task_index]["description"] = updated_description
        tasks[task_index]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_file(tasks) # Save the updated task to file
        print("Task updated successfully.")
    else:
        print("Invalid task number")


def delete_task():
    view_tasks()
    task_index = int(input("Enter the number of the task you want to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_file(tasks) # Save new task list to file
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")
#----------------------------------------------------------------------------------------------------------------------#
def main():
    program = True
    while program:
        user_input = input("Please select an option: (Add/Update/Delete/View/End) ").strip().lower()

        if user_input == "add":
            add_task()
        elif user_input == "update":
            update_task()
        elif user_input == "delete":
            delete_task()
        elif user_input == "view":
            view_tasks()
        elif user_input == "end":
            print("Thank you for using the CLI Task Tracker. Goodbye!")
            program = False


if __name__ == "__main__":
    main()

# TODO 1. Add, Update, and Delete Tasks Functions
# TODO 2. Mark a task as in progress or done Function
# TODO 3. List all tasks Function
# TODO 4. List all tasks that are not done Function
# TODO 5. List all tasks that are in progress Function