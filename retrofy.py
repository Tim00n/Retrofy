import tkinter as tk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import customtkinter

root = tk.Tk()
root.title("Retrofy")
root.geometry("1000x800")
root.iconbitmap("Retrofy.ico")
root.configure(bg='Black')

# Account screen
def open_account():
   games_link.place(width=0, height=0)
   account_link.place(width=0, height=0)
   home_button = customtkinter.CTkButton(master=root, text="Home", command=open_home)
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
   games_link.place(width=0, height=0)
   settings_link.place(width=0, height=0)
   home_button = customtkinter.CTkButton(master=root, text="Home", command=open_home)
   home_button.place(y=655)
   account_link.place(y=695)
   support_link.place(y=730)
# Home screen
def open_home():
      logo_label.destroy()
      bg_label.destroy()
      form_frame.place(width=0, height=0)
      library_label.place(x=0, y=0, relwidth=1, relheight=1)
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
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((2560, 1080))
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tkinter.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
Logo = Image.open("Logo.png")
LogoDisplay = ImageTk.PhotoImage(Logo)
logo_label = tkinter.Label(root, image=LogoDisplay, bd=0)
logo_label.place(x=330, y=170)

library_image = Image.open("library.jpg")
library_image = ImageTk.PhotoImage(library_image)
library_label= tkinter.Label(root, image=library_image)


form_frame = customtkinter.CTkFrame(root, width=300, height=200)
form_frame.place(relx=0.5, rely=0.5, y=150, anchor='center', width=300, height=200)
username_label = customtkinter.CTkLabel(master=form_frame, text="Email:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = customtkinter.CTkEntry(master=form_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label = customtkinter.CTkLabel(master=form_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = customtkinter.CTkEntry(master=form_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button = customtkinter.CTkButton(master=form_frame, text="Login", command=check_credentials)
login_button.grid(row=3, column=1, padx=10, pady=10)

account_link = customtkinter.CTkButton(master=root, text="Account", command=open_account)
support_link = customtkinter.CTkButton(master=root, text="Support", command=open_support)
games_link = customtkinter.CTkButton(master=root, text="Gaming", command=open_game)
settings_link = customtkinter.CTkButton(master=root, text="Settings", command=open_settings)

root.mainloop()