import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()


# Title screen
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



# Creating a login form and database
def check_credentials():
    # Get the values of the username and password fields
    username = frame.username_entry.get()
    password = frame.password_entry.get()

 # Check if the username and password match
    if username == "" and password == "":
        for widget in root.winfo_children():
            widget.destroy()
        # Create a blank page
        library_label = tk.Label(root, text="Welcome")
        library_label.pack()
        
        
    else:
        # Clear the main window
        messagebox.showerror("Login", "Wrong username or password")


# Widgets for the user form (Username, frame, password)
form_frame = tk.Frame(root, bd=2, relief='groove', bg='#87CEFA')
form_frame.place(relx=0.5, rely=0.5, y=150, anchor='center', width=300, height=200)
frame.username_label = tk.Label(form_frame, text="Username:")
frame.username_label.grid(row=0, column=0, padx=10, pady=10)
frame.username_entry = tk.Entry(form_frame)
frame.username_entry.grid(row=0, column=1, padx=10, pady=10)
frame.password_label = tk.Label(form_frame, text="Password:")
frame.password_label.grid(row=1, column=0, padx=10, pady=10)
frame.password_entry = tk.Entry(form_frame, show="*")
frame.password_entry.grid(row=1, column=1, padx=10, pady=10)
frame.login_button = tk.Button(form_frame, text="Login", command=check_credentials, activebackground='#87CEFA')
frame.login_button.place(x=135, y=100)

root.mainloop()
