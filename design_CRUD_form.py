from tkinter import *
from crud_commands import submit, search, update, delete

def create_form_design():
    new_window = Toplevel()
    new_window.geometry("400x400")
    new_window.title("Create")
    new_window.configure(bg="#0B314B")
    name_entry = StringVar()
    last_name_entry = StringVar()
    age_entry = StringVar()
      
    Label(new_window, text="Create operation:", anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=1, padx=20, pady=20)
    # Label and entry widget where the user can input their name
    Label(new_window, text="Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=1, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=name_entry).grid(row = 1, column=1)
    # Label and entry widget where the user can input their last name
    Label(new_window, bd=2, text="Last Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=2, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=last_name_entry).grid(row = 2, column=1)
    # Label and entry widget where the user can input their age
    Label(new_window, text="Age:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=3, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=age_entry).grid(row = 3, column=1)
    # define function to handle button click
    def handle_submit():
        name = name_entry.get()
        last_name = last_name_entry.get()
        age = age_entry.get()
        submit(name, last_name, age)
    # Button to create/adding data
    Button(new_window, text="Submit", bg="#0D5F58", fg="#FEFEFE", 
           font=("Batang", 13), width=10, command=handle_submit).grid(row=4, column=1, padx=5, pady=20)

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
    new_window.geometry("550x450")
    new_window.title("Update")
    new_window.configure(bg="#0B314B")
    Label(new_window, text="Update operation:",anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=1, padx=20, pady=20)
    # Label and entry widget where the user can input their name which they want to update/change
    Label(new_window, text="Name which you \nwant to update/change:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=1, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13)).grid(row = 1, column=1)
    # Search button
    Button(new_window, text="Search", font=("Batang", 13), bg="#166069", 
           fg="#FEFEFE", command=search).grid(row=1, column=3, padx=5, pady=20)
    # Label and entry widget where the user can input their name
    Label(new_window, text="Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=2, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13)).grid(row = 2, column=1)
    # Label and entry widget where the user can input their last name
    Label(new_window, bd=2, text="Last Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=3, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13)).grid(row = 3, column=1)
    # Label and entry widget where the user can input their age
    Label(new_window, text="Age:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=4, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13)).grid(row = 4, column=1)
    # Button to update data
    Button(new_window, text="Update", bg="#0D5F58", fg="#FEFEFE", 
           font=("Batang", 13), width=10, command=update).grid(row=5, column=1, padx=5, pady=20)

def delete_form_design():
    new_window = Toplevel()
    new_window.geometry("500x200")
    new_window.title("Delete")
    new_window.configure(bg="#0B314B")
    name_entry = StringVar()
    Label(new_window, text="Delete operation:",anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=1, padx=20, pady=20)
    # Label and entry widget where the user can input their name which they want to delete
    Label(new_window, text="Name which you \nwant to delete:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=1, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=name_entry).grid(row = 1, column=1)
    # define function to handle button click
    def handle_delete():
        name = name_entry.get()
        delete(name)
    # Button to delete data
    Button(new_window, text="Delete", bg="#0D5F58", fg="#FEFEFE", 
           font=("Batang", 13), width=10, command=handle_delete).grid(row=1, column=2, padx=5, pady=20)