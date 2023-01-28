import tkinter as tk
import customtkinter
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
root = tk.Tk()
# Account screen
def open_account():
   games_link.destroy()
   account_link.destroy()
   home_button = tk.Button(master=root, text="Home", command=open_home)
   sidebar.pack(side="left", fill="both")
   home_button.place(y=655)
   support_link.place(y=695)
   settings_link.place(y=730)
# Select dumped game files
def open_game():
   filepath = filedialog.askopenfilename()
   if filepath:
      os.startfile(filepath)
# Support screen
def open_support():
   print("Working as intended")
# Settings screen
def open_settings():
   games_link.destroy()
   settings_link.destroy()
   home_button = tk.Button(master=root, text="Home", command=open_home)
   sidebar.pack(side="left", fill="both")
   home_button.place(y=655)
   account_link.place(y=695)
   support_link.place(y=730)
# Home screen
def open_home():
      image_label.destroy()
      bg_label.destroy()
      form_frame.destroy()
      sidebar.pack(side="left", fill="both")
      account_link.place(y=655)
      games_link.place(y=695)
      support_link.place(y=730)
      settings_link.place(y=765)
# Login query
def check_credentials():
    # Get the values of the username and password fields
    username = username_entry.get()
    password = password_entry.get()
 # Check if the username and password match
    if username == "" and password == "":
      open_home()
       
    else:
        # Clear the main window
        messagebox.showerror("Login", "Wrong email or password")



# Login screen
root.title("Retrofy")
root.geometry("1000x800")
root.iconbitmap("Retrofy.ico")
Logo = PhotoImage(file="Logo.png")
image_label = tk.Label(root, image=Logo, bd=0, highlightthickness=0, borderwidth=0)
image_label.place(x=330, y=170)
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((2560, 1080))
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
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
login_button = tk.Button(master=form_frame, text="Login", command=check_credentials)
login_button.place(x=110, y=100)

sidebar = tk.Frame(root, width=200, height=400, bg="lightgray")
account_link = tk.Button(master=sidebar, text="Account", command=open_account)
support_link = tk.Button(master=sidebar, text="Support", command=open_support)
games_link = tk.Button(master=sidebar, text="Gaming", command=open_game)
settings_link = tk.Button(master=sidebar, text="Settings", command=open_settings)

root.mainloop()