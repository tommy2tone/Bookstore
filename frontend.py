"""
A program that stores this book information:

Title, Author
Year, ISBN


User can:

View all records
Search an entry
Add entry
Update entry
Delete entry
Close program

"""

from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list_main.curselection()[0]
    selected_tuple = list_main.get(index)
    title_field.delete(0, END)
    title_field.insert(0, selected_tuple[1])
    author_field.delete(0, END)
    author_field.insert(0, selected_tuple[2])
    year_field.delete(0, END)
    year_field.insert(0, selected_tuple[3])
    isbn_field.delete(0, END)
    isbn_field.insert(0, selected_tuple[4])

    
# Button command functions

def view_command():
    list_main.delete(0, END)
    for row in backend.view():
        list_main.insert(END, row)


def search_command():
    list_main.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_main.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_main.delete(0, END)
    list_main.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()
window.wm_title('Bookstore')

# Labels for entry fields

title_label = Label(window, text='Title')
title_label.grid(row=0, column=0)

author_label = Label(window, text='Author')
author_label.grid(row=0, column=2)

year_label = Label(window, text='Year')
year_label.grid(row=1, column=0)

isbn_label = Label(window, text='ISBN')
isbn_label.grid(row=1, column=2)

# Entry fields

title_text = StringVar()
title_field = Entry(window, textvariable=title_text)
title_field.grid(row=0, column=1)

author_text = StringVar()
author_field = Entry(window, textvariable=author_text)
author_field.grid(row=0, column=3)

year_text = StringVar()
year_field = Entry(window, textvariable=year_text)
year_field.grid(row=1, column=1)

isbn_text = StringVar()
isbn_field = Entry(window, textvariable=isbn_text)
isbn_field.grid(row=1, column=3)

# List Box

list_main = Listbox(window, height=6, width=35)
list_main.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar_list_main = Scrollbar(window)
scrollbar_list_main.grid(row=2, column=2, rowspan=6)

list_main.configure(yscrollcommand=scrollbar_list_main)
scrollbar_list_main.configure(command=list_main.yview())

list_main.bind('<<ListboxSelect>>', get_selected_row)

# Buttons

view_all = Button(window, text='View All', width=12, command=view_command)
view_all.grid(row=2, column=3)

search = Button(window, text='Search Entry', width=12, command=search_command)
search.grid(row=3, column=3)

add = Button(window, text='Add Entry', width=12, command=add_command)
add.grid(row=4, column=3)

update = Button(window, text='Update Entry', width=12, command=update_command)
update.grid(row=5, column=3)

delete = Button(window, text='Delete', width=12, command=delete_command)
delete.grid(row=6, column=3)

close = Button(window, text='Close', width=12)
close.grid(row=7, column=3)


window.mainloop()
