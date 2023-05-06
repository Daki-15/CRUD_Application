from tkinter import *

def create():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Create")
    Label(new_window, text="This is a new window for Create operation").pack(padx=20, pady=20)

def read():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Read")
    Label(new_window, text="This is a new window for Read operation").pack(padx=20, pady=20)

def update():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Update")
    Label(new_window, text="This is a new window for Update operation").pack(padx=20, pady=20)

def delete():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Delete")
    Label(new_window, text="This is a new window for Delete operation").pack(padx=20, pady=20)
