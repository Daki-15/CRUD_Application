from tkinter import *
from commands import create, read, update, delete

def form_design(window):
    window.geometry("550x400")
    window.title("Main form")
    window.configure(bg="#0B314B")

def labels_design(window):
    Label(window, text="Hello, this is a simple application that performs\n CRUD(Create, Read, Update, Delete) operations",
           bg="#0B314B", fg="#F4F7F9", anchor="n", font=("Batang", 14)).grid(row=0, column=0, padx=50, pady=50)
    
def buttons_design(window):
    Button(window, text="Create", bg="#186031", fg="#F4F7F9", 
           font=("Batang", 14), width=15, command=create).grid(row=1, column=0, pady=5)
    Button(window, text="Read", bg="#186031", fg="#F4F7F9", 
           font=("Batang", 14), width=15, command=read).grid(row=2, column=0, pady=5)
    Button(window, text="Update", bg="#186031", fg="#F4F7F9", 
           font=("Batang", 14), width=15, command=update).grid(row=3, column=0, pady=5)
    Button(window, text="Delete", bg="#186031", fg="#F4F7F9", 
           font=("Batang", 14), width=15, command=delete).grid(row=4, column=0, pady=5)



