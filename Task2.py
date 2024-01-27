import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=20)

        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.view_all_button = tk.Button(self.root, text="View All Tasks", command=self.view_all_tasks)
        self.view_all_button.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get()
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)
        self.entry_task.delete(0, tk.END)

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if len(selected_task_index) > 0:
            task_index = selected_task_index[0]
            new_task = self.entry_task.get()
            self.tasks[task_index] = new_task
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, new_task)
            self.entry_task.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if len(selected_task_index) > 0:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.task_listbox.delete(task_index)

    def view_all_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()