import tkinter as tk
from tkinter import messagebox

# Initialize the Tkinter window
root = tk.Tk()
root.title("To-Do List")

# Function to add a task
def add_task():
    task = task_entry.get()  # Corrected line
    if task:
        tasks.insert(tk.END, task)  # Add task to the listbox
        task_entry.delete(0, tk.END)  # Clear the entry box
    else:
        messagebox.showwarning("Warning", "You must enter a task.")  # Show warning if no task is entered

# Function to remove a task
def remove_task():
    try:
        task_index = tasks.curselection()[0]  # Get the selected task index
        tasks.delete(task_index)  # Remove the task
    except:
        messagebox.showwarning("Warning", "You must select a task to remove.")  # Show warning if no task is selected

# Function to mark a task as done
def mask_task():
    try:
        task_index = tasks.curselection()[0]  # Get the selected task index
        task = tasks.get(task_index)  # Get the task text
        tasks.delete(task_index)  # Remove the original task
        tasks.insert(tk.END, task + " (done)")  # Insert the task with "(done)" at the end
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")  # Show warning if no task is selected

# Create the Entry widget for entering tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create the Listbox to display tasks
tasks = tk.Listbox(root, width=50, height=10)
tasks.pack(pady=10)

# Create Buttons to add, remove, and mark tasks as done
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", width=20, command=remove_task)
remove_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark Task as Done", width=20, command=mask_task)
mark_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
