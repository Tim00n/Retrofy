import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk


root = tk.Tk()

bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((2560, 1080))
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
sidebar = tk.Frame(root, width=200, bg='#575554')
account_link = tk.Button(sidebar, text="Account", font=("Helvetica", 14), bg='#5A5A5A')
support_link = tk.Button(sidebar, text="Support", font=("Helvetica", 14), bg='#5A5A5A')
games_link = tk.Button(sidebar, text="Gaming", font=("Helvetica", 14), bg='#5A5A5A')
settings_link = tk.Button(sidebar, text="Settings", font=("Helvetica", 14), bg='#5A5A5A')

# Retrofy
root.title("Retrofy")
root.geometry("1000x800")

# Set the icon of the main window
root.iconbitmap("Retrofy.ico")

# Create a PhotoImage object for the new image
Logo = PhotoImage(file="Logo.png")
image_label = tk.Label(root, image=Logo, bd=0, highlightthickness=0, borderwidth=0)
image_label.place(x=330, y=170)



# Creating a login form and database
def check_credentials():
    # Get the values of the username and password fields
    username = username_entry.get()
    password = password_entry.get()
 # Check if the username and password match
    if username == "" and password == "":
       image_label.destroy()
       bg_label.destroy()
       form_frame.destroy()
       sidebar.pack(side=tk.LEFT)
       account_link.pack()
       games_link.pack()
       support_link.pack()
       settings_link.pack()

       
    else:
        # Clear the main window
        messagebox.showerror("Login", "Wrong email or password")
# Login form
form_frame = tk.Frame(root, relief='solid', bg='#333')
form_frame.place(relx=0.5, rely=0.5, y=150, anchor='center', width=300, height=200)
username_label = tk.Label(form_frame, text="Email:", font='Roboto', bg='#333', fg='White')
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label = tk.Label(form_frame, text="Password:", font='Roboto', bg='#333', fg='White')
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button = tk.Button(form_frame, text="Login", font='Roboto', command=check_credentials, activebackground='#87CEFA')
login_button.place(x=135, y=100)

root.mainloop()