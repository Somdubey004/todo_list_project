import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from core import add_task, remove_task, toggle_task_completion
from storage import load_tasks, save_tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.tasks = load_tasks()
        self.icons = self.load_icons()

        self.setup_ui()
        self.render_tasks()

    def load_icons(self):
        base_path = os.path.join(os.path.dirname(__file__), "icons")
        icon_paths = {
            "complete": os.path.join(base_path, "complete.png"),
            "incomplete": os.path.join(base_path, "incomplete.png"),
            "high": os.path.join(base_path, "high.png"),
            "medium": os.path.join(base_path, "medium.png"),
            "low": os.path.join(base_path, "low.png")
        }
        icons = {}
        for key, path in icon_paths.items():
            if os.path.exists(path):
                image = Image.open(path).resize((20, 20))
                icons[key] = ImageTk.PhotoImage(image)
            else:
                icons[key] = None
        return icons

    def setup_ui(self):
        # Top input frame
        top_frame = tk.Frame(self.root, pady=10)
        top_frame.pack(fill=tk.X)

        self.task_entry = tk.Entry(top_frame, font=("Segoe UI", 12))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 5))

        self.priority_var = tk.StringVar(value="medium")
        priority_menu = ttk.Combobox(
            top_frame,
            textvariable=self.priority_var,
            values=["high", "medium", "low"],
            state="readonly",
            font=("Segoe UI", 11),
            width=10
        )
        priority_menu.pack(side=tk.LEFT, padx=(0, 5))

        add_btn = ttk.Button(top_frame, text="Add Task", command=self.add_task)
        add_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Treeview for task display
        self.tree = ttk.Treeview(
            self.root,
            columns=("Status", "Priority", "Task"),
            show="headings",
            height=20
        )
        self.tree.heading("Status", text="Status")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Task", text="Task Name")

        self.tree.column("Status", width=70, anchor="center")
        self.tree.column("Priority", width=80, anchor="w")
        self.tree.column("Task", width=500, anchor="w")

       

        # Bottom buttons
        bottom_frame = tk.Frame(self.root, padx=5)
        bottom_frame.pack(fill=tk.BOTH)

        toggle_btn = ttk.Button(text="Toggle Complete", command=self.toggle_complete)
        toggle_btn.pack(side=tk.BOTTOM, padx=5,pady=10)

        delete_btn = ttk.Button( text="Delete Task", command=self.delete_task)
        delete_btn.pack(side=tk.BOTTOM, padx=10,pady=10)

        self.tree.pack(fill=tk.BOTH, expand=False, padx=10, pady=(0, 100))

    def render_tasks(self):
        self.tree.delete(*self.tree.get_children())

        for idx, task in enumerate(self.tasks):
            status = "✅" if task["completed"] else "❌"
            priority_map = {
                "high": "🔴 High",
                "medium": "🟡 Medium",
                "low": "🟢 Low"
            }
            priority = priority_map.get(task["priority"], "🟢 Low")

            self.tree.insert("", "end", iid=idx, values=(status, priority, task["task_name"]))

    def add_task(self):
        name = self.task_entry.get().strip()
        priority = self.priority_var.get().lower()

        if not name:
            messagebox.showwarning("Input Error", "Please enter a task name.")
            return

        add_task(self.tasks, name, priority)
        save_tasks(self.tasks)
        self.task_entry.delete(0, tk.END)
        self.render_tasks()

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("No Selection", "Please select a task to delete.")
            return
        index = int(selected_item[0])
        remove_task(self.tasks, index)
        save_tasks(self.tasks)
        self.render_tasks()

    def toggle_complete(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("No Selection", "Please select a task to toggle completion.")
            return
        index = int(selected_item[0])
        toggle_task_completion(self.tasks, index)
        save_tasks(self.tasks)
        self.render_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
