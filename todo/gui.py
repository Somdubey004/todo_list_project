import tkinter as tk
from tkinter import ttk, messagebox
from core import *
from storage import *
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("700x500")

        # Set app icon
        self.root.iconphoto(False, tk.PhotoImage(file="icons/app_icon.png"))

        # Load tasks
        self.tasks = load_tasks()

        # Load icons
        self.icons = {
            "high": tk.PhotoImage(file="icons/high.png"),
            "medium": tk.PhotoImage(file="icons/medium.png"),
            "low": tk.PhotoImage(file="icons/low.png"),
            "complete": tk.PhotoImage(file="icons/complete.png"),
            "incomplete": tk.PhotoImage(file="icons/incomplete.png")
        }

        # Top input frame
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.priority_var = tk.StringVar(value="medium")
        self.priority_menu = ttk.Combobox(root, textvariable=self.priority_var, values=["high", "medium", "low"], width=10)
        self.priority_menu.grid(row=0, column=1, padx=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=5)

        # Task list area
        self.tree = ttk.Treeview(root, columns=("status", "priority", "name"), show='tree')
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.tree.column("#0", width=600)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky="ns")

        # Buttons
        self.toggle_button = tk.Button(root, text="Toggle Complete", command=self.toggle_complete)
        self.toggle_button.grid(row=2, column=0, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, pady=10)

        # Show initial tasks this is new change
        self.update_tree()

    def get_icon(self, key):
        return self.icons.get(key, None)

    def update_tree(self):
        self.tree.delete(*self.tree.get_children())
        for idx, task in enumerate(self.tasks):
            status_icon = "complete" if task["completed"] else "incomplete"
            priority_icon = task["priority"]
            icon = self.get_icon(status_icon)
            priority = self.get_icon(priority_icon)
            task_text = f"{task['task_name']}"

            # Display as: [status icon] [priority icon] Task Name
            self.tree.insert("", "end", iid=idx, text=task_text, image=icon)

    def add_task(self):
        name = self.entry.get().strip()
        priority = self.priority_var.get().lower()

        if not name:
            messagebox.showwarning("Input Error", "Task name cannot be empty.")
            return

        add_task(self.tasks, name, priority)
        save_tasks(self.tasks)
        self.update_tree()
        self.entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Selection Error", "Please select a task to delete.")
            return

        index = int(selected[0])
        remove_task(self.tasks, index)
        save_tasks(self.tasks)
        self.update_tree()

    def toggle_complete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Selection Error", "Please select a task to toggle.")
            return

        index = int(selected[0])
        toggle_task_completion(self.tasks, index)
        save_tasks(self.tasks)
        self.update_tree()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
