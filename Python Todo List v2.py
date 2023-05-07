import os
import tkinter as tk

filename = "todos.txt"

# Load the todo list from file if it exists
if os.path.exists(filename):
    with open(filename, "r") as f:
        todos = [line.strip() for line in f.readlines()]
else:
    todos = []

# Define a function to add a new todo to the list
def add_todo():
    todo = new_todo_entry.get()
    todos.append(todo)
    update_listbox()
    new_todo_entry.delete(0, tk.END)

# Define a function to remove a todo from the list
def remove_todo():
    selected_index = listbox.curselection()[0]
    del todos[selected_index]
    update_listbox()

# Define a function to update the listbox with the current todos
def update_listbox():
    listbox.delete(0, tk.END)
    for todo in todos:
        listbox.insert(tk.END, todo)

# Create the main window
root = tk.Tk()
root.title("Todo List")

# Create a label and an entry for adding new todos
new_todo_label = tk.Label(root, text="New Todo:")
new_todo_label.pack(side=tk.LEFT, padx=5, pady=5)
new_todo_entry = tk.Entry(root)
new_todo_entry.pack(side=tk.LEFT, padx=5, pady=5)
new_todo_entry.bind("<Return>", lambda event: add_todo())

# Create a button to add new todos
add_button = tk.Button(root, text="Add", command=add_todo)
add_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create a listbox to display the current todos
listbox = tk.Listbox(root, height=20, width=50)
listbox.pack(side=tk.LEFT, padx=5, pady=5)
update_listbox()

# Create a button to remove selected todos
remove_button = tk.Button(root, text="Remove", command=remove_todo)
remove_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create a function to save the todo list to file before exiting
def on_closing():
    with open(filename, "w") as f:
        f.write("\n".join(todos))
    root.destroy()

# Add a protocol to handle the window closing event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the main event loop
root.mainloop()
