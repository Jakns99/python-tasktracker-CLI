import os
import json
from datetime import datetime


print("\033[1mWelcome to the CLI Task Tracker.\033[0m")
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
        print_error(f"Error saving tasks file: {e}")

def load_file():
    """Load tasks from a JSON file."""
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except Exception as e:
            print_error(f"Error loading tasks file: {e}")
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
        print_error("Please enter a valid number. (1. todo, 2. in-progress, 3. done)")

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
        print_error("Invalid task number")


def delete_task():
    view_tasks()
    task_index = int(input("Enter the number of the task you want to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_file(tasks) # Save new task list to file
        print("Task deleted successfully.")
    else:
        print_error("Invalid task number.")
#----------------------------------------------------------------------------------------------------------------------#
def print_error(message):
    """Emboldens the error message"""
    print(f"\033[1;31m{message}\033[0m")  # Bold red text

def main():
    program = True
    while program:
        print("\n\033[1mOptions:\033[0m")
        print("#-----------------------------------------------------------------------------------------------------#")
        print("\n\033[1mAdd:\033[0m Add a new task to the task list.")
        print("\033[1mUpdate:\033[0m Update an existing task.")
        print("\033[1mDelete:\033[0m Delete an existing task.")
        print("\033[1mView:\033[0m View all tasks.")
        print("\033[1mEnd:\033[0m End the program.\n")
        print("#-----------------------------------------------------------------------------------------------------#")
        user_input = input("\033[1mPlease select an option: (Add/Update/Delete/View/End)\033[0m ").strip().lower()

        if user_input == "add":
            add_task()
        elif user_input == "update":
            update_task()
        elif user_input == "delete":
            delete_task()
        elif user_input == "view":
            view_tasks()
        elif user_input == "end":
            print("\033[1mThank you for using the CLI Task Tracker. Goodbye!\033[0m")
            program = False
        else:
            print_error("\nInvalid input. Please try again.")


if __name__ == "__main__":
    main()

# TODO 1. Add, Update, and Delete Tasks Functions (DONE)
# TODO 2. Mark a task as in progress or done Function
# TODO 3. List all tasks Function
# TODO 4. List all tasks that are not done Function
# TODO 5. List all tasks that are in progress Function