import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Create GUI components
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=1, column=0, padx=5, pady=10)

        self.display_button = tk.Button(master, text="Display Tasks", command=self.display_tasks)
        self.display_button.grid(row=1, column=1, padx=5, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Task Added", f'Task "{task}" added to the to-do list.')
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        task = self.task_entry.get()
        if task in self.tasks:
            self.tasks.remove(task)
            messagebox.showinfo("Task Removed", f'Task "{task}" removed from the to-do list.')
        else:
            messagebox.showwarning("Task Not Found", f'Task "{task}" not found in the to-do list.')

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Empty To-Do List", "The to-do list is empty.")
        else:
            tasks_text = "\n".join([f"{index + 1}. {task}" for index, task in enumerate(self.tasks)])
            messagebox.showinfo("To-Do List", tasks_text)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
