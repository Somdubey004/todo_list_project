from colorama import Fore
from storage import *
from utils import *

def add_task(tasks, name, priority="medium"):
    """
    Add a new task to the list.

    Args:
        tasks (list): The list of existing tasks.
        name (str): The name of the new task.
        priority (str): The priority level of the task (high/medium/low).
    """
    task = {
        "task_name": name,
        "completed": False,
        "priority": priority.lower()
    }
    tasks.append(task)


def remove_task(tasks, index):
    """
    Remove a task from the list by its index.

    Args:
        tasks (list): The list of tasks.
        index (int): The index of the task to remove.
    """
    if 0 <= index < len(tasks):
        tasks.pop(index)


def toggle_task_completion(tasks, index):
    """
    Toggle the completion status of a task.

    Args:
        tasks (list): The list of tasks.
        index (int): The index of the task to toggle.
    """
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = not tasks[index]["completed"]


# def add_task(task_list, task_name, priority):
#     task = {
#         "task_name": task_name,
#         "completed": False,
#         "priority": priority
#     }
#     task_list.append(task)
#     save_tasks(task_list)

# def remove_task(task_list, index):
#     if 0 <= index < len(task_list):
#         task_list.pop(index)
#         save_tasks(task_list)

# def toggle_task_completion(task_list, index):
#     if 0 <= index < len(task_list):
#         task_list[index]["completed"] = not task_list[index]["completed"]
#         save_tasks(task_list)

# def view_tasks(task_list):  # optional CLI view
#     if not task_list:
#         print("No tasks to show.")
#         return
#     print("\n--- To-Do List ---")
#     for index, task in enumerate(task_list, start=1):
#         print(f"[{index}] {format_task_display(task)}")


# def add_task(task_list):
#     task_name = input("Enter task name: ")

#     # Ask for priority
#     priority = ""
#     while priority not in ["high", "medium", "low"]:
#         priority = input("Set priority [high / medium / low]: ").lower()
#         if priority not in ["high", "medium", "low"]:
#             print("Invalid priority. Please enter high, medium, or low.")

#     task = {
#         "task_name": task_name,
#         "completed": False,
#         "priority": priority
#     }

#     task_list.append(task)
#     save_tasks(task_list)
#     print(Fore.GREEN + "Task added successfully!")

# def view_tasks(task_list):
#     if not task_list:
#         print(Fore.YELLOW + "No tasks to show.")
#         return
#     print(Fore.CYAN + "\n--- To-Do List ---")
#     for index, task in enumerate(task_list, start=1):
#         print(f"[{index}] {format_task_display(task)}")

# def remove_task(task_list):
#     view_tasks(task_list)
#     try:
#         task_num = int(input("Enter task number to remove: "))
#         if 1 <= task_num <= len(task_list):
#             removed = task_list.pop(task_num - 1)
#             save_tasks(task_list)
#             print(Fore.GREEN + f"Removed task: {removed['task_name']}")
#         else:
#             print(Fore.RED + "Invalid task number.")
#     except ValueError:
#         print(Fore.RED + "Please enter a valid number.")

# def toggle_task_completion(task_list):
#     view_tasks(task_list)
#     try:
#         task_num = int(input("Enter task number to toggle complete/incomplete: "))
#         if 1 <= task_num <= len(task_list):
#             task = task_list[task_num - 1]
#             task["completed"] = not task["completed"]
#             save_tasks(task_list)
#             print(Fore.GREEN + f"Marked task as {'complete' if task['completed'] else 'incomplete'}.")
#         else:
#             print(Fore.RED + "Invalid task number.")
#     except ValueError:
#         print(Fore.RED + "Please enter a valid number.")
