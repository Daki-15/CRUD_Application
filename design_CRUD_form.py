from tkinter import *
from crud_commands import submit, search, update, delete, all_data_from_data_base

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
    # Create a new window
    new_window = Toplevel()
    # Set the dimensions of the window
    new_window.geometry("420x350")
    # Set the title of the window
    new_window.title("Read")
    # Set the background color of the window
    new_window.configure(bg="#0B314B")
    
    # Add a label to the window
    Label(new_window, text="Read operation:", anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row=0, column=0, padx=5, pady=10)
    
    # Get all data from the database
    Data = all_data_from_data_base()
    # Create an empty list to store the data for each person
    list_of_all_people = []
    
    # Loop through each person in the data
    for person in Data:
        # Add a list of the person's data to the list_of_all_people list
        list_of_all_people.append([person["name"], person["last_name"], person["age"]])
      
    # Create a StringVar object initialized with the list_of_all_people
    data_var = StringVar(value=list_of_all_people)
    # Create a Listbox widget using the data_var as its listvariable
    Listbox(new_window, width=60, height=15, listvariable=data_var).grid(row=1, column=0, padx=20, pady=20)



def update_form_design():
    new_window = Toplevel()
    new_window.geometry("550x450")
    new_window.title("Update")
    new_window.configure(bg="#0B314B")
    searched_name = StringVar()
    name_entry = StringVar()
    last_name_entry = StringVar()
    age_entry = StringVar()

    Label(new_window, text="Update operation:",anchor="n", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 15)).grid(row = 0, column=1, padx=20, pady=20)
    # Label and entry widget where the user can input their name which they want to update/change
    Label(new_window, text="Name which you \nwant to update/change:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=1, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=searched_name).grid(row = 1, column=1)
    # define function to handle button click
    def handle_search():
        name = searched_name.get()
        data = search(name)
        name_entry.set(data[0])
        last_name_entry.set(data[1])
        age_entry.set(data[2])
    # Search button
    Button(new_window, text="Search", font=("Batang", 13), bg="#166069", 
           fg="#FEFEFE", command=handle_search).grid(row=1, column=3, padx=5, pady=20)
    # Label and entry widget where the user can input their name
    Label(new_window, text="Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=2, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=name_entry).grid(row = 2, column=1)
    # Label and entry widget where the user can input their last name
    Label(new_window, bd=2, text="Last Name:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=3, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=last_name_entry).grid(row = 3, column=1)
    # Label and entry widget where the user can input their age
    Label(new_window, text="Age:", anchor="w", 
          bg="#0B314B", fg="#F4F7F9", font=("Batang", 13)).grid(row=4, column=0, padx=5, pady=20)
    Entry(new_window, bd=2, font=("Batang", 13), textvariable=age_entry).grid(row = 4, column=1)
    # define function to handle button click
    def handle_update():
        name = searched_name.get()
        new_name = name_entry.get()
        new_last_name = last_name_entry.get()
        new_age = age_entry.get()
        update(name, new_name, new_last_name, new_age)
    # Button to update data
    Button(new_window, text="Update", bg="#0D5F58", fg="#FEFEFE", 
           font=("Batang", 13), width=10, command=handle_update).grid(row=5, column=1, padx=5, pady=20)

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