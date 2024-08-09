# todo_list_gui.py

import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.root = tk.Tk()
        self.root.title("To-Do List")

        # Create task list frame
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill="both", expand=True)

        # Create task list
        self.task_list = tk.Listbox(self.task_list_frame)
        self.task_list.pack(fill="both", expand=True)

        # Create entry field for new tasks
        self.new_task_entry = tk.Entry(self.root)
        self.new_task_entry.pack()

        # Create buttons
        self.create_task_button = tk.Button(self.root, text="Create Task", command=self.create_task)
        self.create_task_button.pack()

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.mark_task_completed_button = tk.Button(self.root, text="Mark Task Completed", command=self.mark_task_completed)
        self.mark_task_completed_button.pack()

        self.display_tasks_button = tk.Button(self.root, text="Display Tasks", command=self.display_tasks)
        self.display_tasks_button.pack()

    def create_task(self):
        task_name = self.new_task_entry.get()
        if task_name not in self.tasks:
            self.tasks[task_name] = False
            self.task_list.insert("end", task_name)
            self.new_task_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Task already exists!")

    def update_task(self):
        task_name = self.task_list.get("active")
        new_task_name = self.new_task_entry.get()
        if task_name in self.tasks:
            self.tasks[new_task_name] = self.tasks.pop(task_name)
            self.task_list.delete("active")
            self.task_list.insert("end", new_task_name)
            self.new_task_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Task not found!")

    def delete_task(self):
        task_name = self.task_list.get("active")
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.task_list.delete("active")
        else:
            messagebox.showerror("Error", "Task not found!")

    def mark_task_completed(self):
        task_name = self.task_list.get("active")
        if task_name in self.tasks:
            self.tasks[task_name] = True
            self.task_list.delete("active")
            self.task_list.insert("end", f"[Completed] {task_name}")
        else:
            messagebox.showerror("Error", "Task not found!")

    def display_tasks(self):
        self.task_list.delete(0, "end")
        for task, status in self.tasks.items():
            if status:
                self.task_list.insert("end", f"[Completed] {task}")
            else:
                self.task_list.insert("end", task)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()