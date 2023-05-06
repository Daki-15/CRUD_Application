from tkinter import *
from design_main_form import form_design, labels_design, buttons_design

def main():
    window = Tk()
    form_design(window)
    labels_design(window)
    buttons_design(window)
    window.mainloop()

if __name__ == "__main__":
    main()
