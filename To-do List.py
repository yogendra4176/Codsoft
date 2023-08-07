from tkinter import *
root = Tk()
root.title('TechVidvan To-Do List')
root.geometry('300x400')
root.config(bg="mediumorchid")
tasks_list=[]
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()
    listbox.insert(END, new_task)
    tasks_list.append(new_task)
    new.delete(0,END)

def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)
    for line in tasks_list:
        if listbox.get(ACTIVE) == line[:-2]:
            tasks_list.remove(line)
    new.delete(0,END)

L1=Label(root, text='My To Do List', bg='red', font=("Times", 15), wraplength=300)
L1.place(x=90, y=10)
tasks = Listbox(root, selectbackground='green', bg='beige', font=('verdana', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=50, height=232)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=50)
for task in tasks_list:
    tasks.insert(END, task)
new= Entry(root, width=37)
new.place(x=35, y=310)
add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('verdana', 12),command=lambda: add_item(new, tasks))
add_btn.place(x=45, y=350)
delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('verdana', 12),command=lambda: delete_item(tasks))
delete_btn.place(x=150, y=350)
root.update()
root.mainloop()