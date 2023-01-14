import tkinter as tk
from tkinter import messagebox
from tkinter import *

root = tk.Tk()
root.config(bg='grey')
root.title("Retrofy")

# Set the icon of the main window
root.iconbitmap("Retrofy.ico")

# Create a PhotoImage object for the new image
image = PhotoImage(file="Retrofy.png")

# Create a Label widget to display the image
image_label = tk.Label(root, image=image)
image_label.pack()
image_label.config(bg='grey')

first_page = tk.Frame(root)

def new_screen():
    current_screen.grid_forget()
    new_screen.grid(row=0, column=0, sticky="nsew")

# Creating a login form and database
def check_credentials():
    # Get the values of the username and password fields
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password match
    if username == "admin" and password == "password":
        print('Phil ist nett')

    else:
        messagebox.showerror("Login", "Do you even lift bro?")


# Widgets for the user form (Username, frame, password)
form_frame = tk.Frame(root, bd=2, relief='groove', bg='#87CEFA')
form_frame.place(relx=0.5, rely=0.5, y=150, anchor='center', width=300, height=200)
username_label = tk.Label(form_frame, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label = tk.Label(form_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button = tk.Button(form_frame, text="Login", command=check_credentials, activebackground='#87CEFA')
login_button.place(x=135, y=100)

# Buttons
controller = None
var = tk.IntVar()
guest_button = tk.Button(form_frame, text="Guest", activebackground='#87CEFA')
guest_button.place(x=135, y=140)

root.mainloop()
