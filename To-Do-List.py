import os
import tkinter as tk

task_list = []
save = "savefile.txt"

def savefile():
    with open(save, "w") as file:
        for task in task_list:
            file.write(task + "\n")
def loadfile():
    try:
        with open(save, "r") as file:
            for line in file:
                task_list.append(line.strip())
    except FileNotFoundError:
        print("No save file found. Starting fresh.")
def add():
    task = new_task.get()
    if task:
        task_list.append(task + "-pending")
        new_task.delete(0, tk.END)
        update_display()
def remove():
    selected = tasks.curselection()
    if selected:
        task_list.pop(selected[0])
        update_display()
def markdone():
    selected = tasks.curselection()
    if selected:
        task_list[selected[0]] = task_list[selected[0]].replace("-pending", "-done")
        update_display()
def update_display():
    tasks.delete(0, tk.END)
    for i, task in enumerate(task_list, start=1):
        tasks.insert(tk.END,f"{i}. {task}\n")
    savefile()

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("480x480")

tk.Label(root, text="Add new task:").pack(pady=5)

new_task = tk.Entry(root, width=50)
new_task.pack(pady=5)

add_button = tk.Button(root, text="Add", command=add)
add_button.pack(pady=2)
remove_button = tk.Button(root, text="Remove", command=remove)
remove_button.pack(pady=2)
markdone_button = tk.Button(root, text="Mark Done", command=markdone)
markdone_button.pack(pady=2)

tasks = tk.Listbox(root, width=50, height=15)
tasks.pack(pady=5)

loadfile()
update_display()

root.mainloop()

