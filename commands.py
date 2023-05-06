from tkinter import *

# define a function to create a new record
def create():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Create")
    Label(new_window, text="This is a new window for Create operation").pack(padx=20, pady=20)

# define a function to read a record
def read():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Read")
    Label(new_window, text="This is a new window for Read operation").pack(padx=20, pady=20)

# define a function to update a record
def update():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Update")
    Label(new_window, text="This is a new window for Update operation").pack(padx=20, pady=20)

# define a function to delete a record
def delete():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Delete")
    Label(new_window, text="This is a new window for Delete operation").pack(padx=20, pady=20)
