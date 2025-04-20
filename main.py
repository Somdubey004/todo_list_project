from colorama import Fore

def format_task_display(task):
    completed = task["completed"]
    name = task["task_name"]
    priority = task["priority"]

    if priority == "high":
        priority_label = Fore.RED + "🟥 High"
    elif priority == "medium":
        priority_label = Fore.YELLOW + "🟨 Medium"
    else:
        priority_label = Fore.GREEN + "🟩 Low"

    if completed:
        name = "\u0336".join(name) + "\u0336"

    status = "✅" if completed else "❌"
    return f"{status} {priority_label} - {name}"