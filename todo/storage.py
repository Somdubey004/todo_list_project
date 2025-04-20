import json
import os

DATA_FILE = "todo_data.json"
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(task_list):
    with open(DATA_FILE, "w") as file:
        json.dump(task_list, file, indent=4)
