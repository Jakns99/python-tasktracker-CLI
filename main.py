import os
import json

# JSON Functionality
#----------------------------------------------------------------------------------------------------------------------#
TASK_FILE = "tasks.json"

def savefile(tasks):
    """Save tasks to a JSON file."""
    try:
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks file: {e}")

def loadfile():
    """Load tasks from a JSON file."""
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error, file not found.")
            return []
#----------------------------------------------------------------------------------------------------------------------#








# TODO 1. Add, Update, and Delete Tasks Functions
# TODO 2. Mark a task as in progress or done Function
# TODO 3. List all tasks Function
# TODO 4. List all tasks that are not done Function
# TODO 5. List all tasks that are in progress Function