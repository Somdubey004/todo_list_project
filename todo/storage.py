import json
import os

import json
import os

# Location of the JSON file to store tasks
STORAGE_FILE = "data/todo_data.json"

def load_tasks():
    """
    Load tasks from the JSON file.

    Returns:
        list: List of task dictionaries.
    """
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # fallback if file is empty or malformed

def save_tasks(tasks):
    """
    Save the task list to the JSON file.

    Args:
        tasks (list): List of task dictionaries.
    """
    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
    with open(STORAGE_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# DATA_FILE = "todo_data.json"
# def load_tasks():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as file:
#             return json.load(file)
#     return []

# def save_tasks(task_list):
#     with open(DATA_FILE, "w") as file:
#         json.dump(task_list, file, indent=4)
