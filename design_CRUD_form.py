from tkinter import *

def create_form_design():
    new_window = Toplevel()
    new_window.geometry("400x300")
    new_window.title("Create")
    new_window.configure(bg="#0B314B")
    Label(new_window, text="Create operation:", anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=1, padx=20, pady=20)
    # Label and entry widget where the user can input their name
    Label(new_window, text="Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=1, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13)).grid(row = 1, column=1)
    # Label and entry widget where the user can input their last name
    Label(new_window, bd=2, text="Last Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=2, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13)).grid(row = 2, column=1)
    # Label and entry widget where the user can input their age
    Label(new_window, text="Age:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=3, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13)).grid(row = 3, column=1)

def read_form_design():
    new_window = Toplevel()
    new_window.geometry("420x350")
    new_window.title("Read")
    new_window.configure(bg="#0B314B")
    Label(new_window, text="Read operation:", anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=0, padx=5, pady=10)
    Listbox(new_window, width=60, height=15).grid(row = 1, column=0, padx=20, pady=20)

def update_form_design():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Update")
    new_window.configure(bg="#0B314B")
    Label(new_window, text="Update operation:",anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=1, padx=20, pady=20)

def delete_form_design():
    new_window = Toplevel()
    new_window.geometry("400x200")
    new_window.title("Delete")
    new_window.configure(bg="#0B314B")
    Label(new_window, text="Delete operation:",anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=1, padx=20, pady=20)